"""LLM related functions."""
import base64
import json
import re

from openai import OpenAI
from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
    HarmBlockThreshold,
    HarmCategory,
    Part,
)

from src.io import logger


# flake8: noqa
# pylint: disable=all
class LlmClient:
    """A client for interacting with large language models (LLMs)."""

    def __init__(self, openai_key=None, parameters=None):
        """Initialize the LLM client."""
        # Initialize the model parameters
        self.model_params = {
            "temperature": parameters.get("temperature", 0),
            "max_output_tokens": parameters.get("maxOutputTokens", 8000),
            "top_p": parameters.get("top_p", 0.8),
            "top_k": parameters.get("top_k", 40),
            "seed": parameters.get("seed", 42),
            "response_mime_type": "application/json",
        }
        self.model_id = parameters.get("model_id", "gemini-1.5-pro-001")
        # Initialize the safety configuration
        self.safety_config = {
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        }
        # Initialize the Gemini client
        self.geminy_client = self._initialize_gemini()
        if openai_key is not None:
            # Initialize the ChatGPT client
            self.chatgpt_client = self._create_client_chatgpt(openai_key)

    def _initialize_gemini(self):
        """Ask the Gemini model a question.

        Returns:
            str: The response from the model.
        """
        # Initialize the model if it is not already initialized
        model_gen = GenerativeModel(model_name=self.model_id)
        self.model_config = GenerationConfig(**self.model_params)

        return model_gen

    def _create_client_chatgpt(self, openai_key):
        client = OpenAI(
            base_url="https://api.langdock.com/openai/eu/v1", api_key=openai_key
        )
        return client

    def ask_gemini(self, prompt: str, document: str = None, response_schema: dict = None):
        """Ask the Gemini model a question.

        Args:
            prompt (str): The prompt to send to the model.
            document (str, optional): An optional document to provide context.
            response_schema (dict, optional): Defines a specific response schema for the model.

        Returns:
            str: The response from the model.
        """
        try:
            # Start with the default model configuration
            config = self.model_config

            # Add response_schema if provided. This is only supported for Gemini 1.5 Flash & Pro models
            if response_schema is not None and "1.5" in self.model_id:
                config = GenerationConfig(
                    response_schema=response_schema,
                    **self.model_params
                )

            # Prepare inputs for the model
            inputs = [document, prompt] if document else prompt

            # Generate the response
            model_response = self.geminy_client.generate_content(
                contents=inputs,
                generation_config=config,
                stream=document is not None,
                safety_settings=self.safety_config
            )

            response_text = ""
            if document:
                for response in model_response:
                    response_text += response.text
            else:
                response_text = model_response.text

            return response_text

        except Exception as e:
            raise RuntimeError(f"Failed to generate response: {str(e)}")

    def clean_llm_response(self, response):
        """Clean the response from LLM to get a valid JSON.

        This function searches for a JSON block within a response, extracts it,
        and replaces single quotes with double quotes. It also removes newline
        characters to ensure the JSON is formatted as a single line.

        Args:
            response (str): The raw response string from LLM.

        Returns:
            str: A cleaned and formatted JSON string extracted from the response.
        """
        # Search for a JSON block within the response
        match = re.search(r'```json\s*(.*?)\s*```', response, re.DOTALL) or \
                re.search(r'```\s*(.*?)\s*```', response, re.DOTALL) or \
                re.search(r'\{.*\}', response, re.DOTALL)

        if match:
            # Extract the JSON block from the response
            response = match.group(1) if match.lastindex else match.group(0)

        return response.replace("'", "\"").replace("\n", " ").replace("\\n", " ").strip()

    def clean_quotes_from_json(self, response):
        """Clean unnecessary quotes from a JSON string within a response.

        This function processes a response string to remove quotes that are not
        needed for JSON keys or values, ensuring valid JSON formatting. It
        specifically targets quotes that appear around keys or structural
        elements like colons and commas.

        Args:
            response (str): The raw response string containing JSON data.

        Returns:
            cleaned_response (str): A cleaned JSON string with unnecessary quotes removed.
        """
        cleaned_list = []
        response = response.replace('{ "', '{"')
        response = response.replace('" }', '"}')
        first_ix = response.index('{"') + 1
        end_ix = response.index('{"') + 1
        for ix, char in enumerate(response[first_ix:]):
            if char == '"':
                prev_char = response[first_ix + ix - 1]
                next_char = response[first_ix + ix + 1]
                # if next_char.isalnum() or next_char.isspace():
                if next_char in [":", ",", "}"] or prev_char in [" ", ",", "{", "\\"]:
                    start_ix = end_ix
                    end_ix = ix + 2
                    cleaned_list.append(response[start_ix:end_ix])
                else: # next_char.isalnum() and prev_char.isalnum():
                    start_ix = end_ix
                    end_ix = ix + 2
                    cleaned_list.append(response[start_ix:end_ix])
                    end_ix += 1

        # TODO: find a more generic way to do this
        # problem is if the last value is null
        if cleaned_list[-1] == '"vgmCutOff':
            cleaned_list.append('": null}')
            cleaned_response = '{' + "".join(cleaned_list)  # noqa
        else:
            cleaned_response = '{' + "".join(cleaned_list) + '"}]}'  # noqa
        return cleaned_response

    def get_unified_json_genai(self, prompt, document=None, response_schema=None):
        """Send a prompt to a Google Cloud AI Platform model and returns the generated json.

        Args:
            prompt (str): The prompt to send to the LLM model.
            document: Content of the PDF document
            response_schema: The schema to use for the response

        Returns:
            dict: The generated json from the model.
        """
        # Ask the LLM model
        response = self.ask_gemini(prompt, document, response_schema)

        try:
            return json.loads(response)
        except json.decoder.JSONDecodeError as e:
            logger.error(e)
            return {}

    def prepare_document_for_gemini(self, file_content):
        """Prepare a document from file content by encoding it to base64.

        Args:
            file_content (bytes): The binary content of the file to be processed.

        Returns:
            Part: A document object ready for processing by the language model.
        """
        # Convert binary file to base64
        pdf_base64 = base64.b64encode(file_content).decode("utf-8")

        # Create the document for the model
        document = Part.from_data(
            mime_type="application/pdf", data=base64.b64decode(pdf_base64)
        )

        return document

    def ask_chatgpt(self, prompt: str, document=None):
        """Ask the chatgpt model a question.

        Args:
            prompt (str): The prompt to ask the model.
            document (base64): the image to send the model
        Returns:
            str: The response from the model.
        """
        # Check if chatgpt_client was initialised
        if self.chatgpt_client is None:
            logger.error("Attempting to call chatgpt model that was not initialised.")
            return ""
        if document is None:
            completion = self.chatgpt_client.chat.completions.create(
                model="gpt-4o",
                temperature=0.1,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt,
                            }
                        ],
                    }
                ],
            )
        else:
            completion = self.chatgpt_client.chat.completions.create(
                model="gpt-4o",
                temperature=0.1,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt,
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{document}",
                                },
                            },
                        ],
                    }
                ],
            )

        response = completion.choices[0].message.content
        return response

    def get_unified_json_chatgpt(self, prompt, document=None):
        """Send a prompt to a Google Cloud AI Platform model and returns the generated json.

        Args:
            prompt (str): The prompt to send to the LLM model.
            parameters (dict, optional): The parameters to use for the model. Defaults to None.

        Returns:
            dict: The generated json from the model.
        """
        # Ask the LLM model
        response = self.ask_gemini(prompt, document)
        cleaned_response = self.clean_llm_response(response)

        try:
            response_json = json.loads(cleaned_response)
        except json.decoder.JSONDecodeError:
            try:
                cleaned_response = self.clean_quotes_from_json(cleaned_response)
                response_json = json.loads(cleaned_response)
            # for excel logic
            except json.JSONDecodeError:
                # Replace single quotes with double quotes
                cleaned_response = re.sub(r"(?<!\\)'", '"', cleaned_response)
                response_json = json.loads(cleaned_response)
        return response_json


def prompt_excel_extraction(excel_structured_text):
    """Write a prompt to extract data from Excel files.

    Args:
        excel_structured_text (str): The structured text of the Excel file.

    Returns:
        prompt str: The prompt for common json.
    """
    prompt = f"""{excel_structured_text}

    Task: Fill in the following dictionary from the information in the given in the above excel data.

    Instructions:
    - Do not change the keys of the following dictionary.
    - The values should be filled in as per the schema provided below.
    - If an entity contains a 'display_name', consider its properties as child data points in the below format.
    {{'data-field': {{
        'child-data-field': 'type -occurrence_type- description',
          }}
    }}
    - The entity with 'display_name' can be extracted multiple times. Please pay attention to the occurrence_type.
    - Ensure the schema reflects the hierarchical relationship.
    - Use the data field description to understand the context of the data.

    """
    return prompt


# pylint: enable=all
