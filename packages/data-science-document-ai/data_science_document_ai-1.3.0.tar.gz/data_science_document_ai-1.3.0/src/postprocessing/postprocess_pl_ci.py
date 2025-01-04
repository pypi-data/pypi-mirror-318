"""This module contains the post-processing work for the packingList and commercialInvoice document."""
from src.utils import generate_schema_structure, get_data_set_schema, get_processor_name


async def get_sku_doc_ai_schema(params, schema_client, input_doc_type):
    """Get the SKU schema of the document from the Document AI processor.

    Args:
        params (dict): The project parameters.
        schema_client (object): The schema client object.
        input_doc_type (str): The document type.

    Returns:
        entity (object): The entity type of the document.
        str: The name of the entity
    """
    processor_name = await get_processor_name(params, input_doc_type)
    # Get the schema of a processor and select only the entity types
    schema = await get_data_set_schema(schema_client, name=processor_name)

    # Find the entity type with the name "skuData" or "skus" and return it
    for entity in schema.document_schema.entity_types:
        if entity.name == "skuData" or entity.name == "skus":
            return entity, entity.name

    return None, None


async def process_file_w_llm(
    params, schema_sku, file_content, llm_client, response_schema
):
    """Process a document using a large language model to extract structured data.

    Args:
        params (dict): The project parameters.
        schema_sku (object): The schema of the SKU data.
        file_content (str): The content of the file to be processed.
        llm_client (object): The LLM client object.
        response_schema (object): The schema of the response data.

    Returns:
        result (dict): The structured data extracted from the document, formatted as JSON.
    """
    # convert file_content to required document
    document = llm_client.prepare_document_for_gemini(file_content)

    # Create a prompt for the task along with the schema
    prompt = await prompt_sku_extraction(schema_sku)

    # Extract data using the LLM
    response = llm_client.get_unified_json_genai(
        prompt, document=document, response_schema=response_schema
    )

    return response, params["gemini_params"]["model_id"]


# flake8: noqa
# pylint: disable=all
async def prompt_sku_extraction(schema):
    """Write a prompt to extract data from PL and CI documents.

    Args:
        schema (str): The schema of the data to extract

    Returns:
        prompt str: The prompt for common json.
    """
    pl = """
    - If containerNumber, sealNumber, poNumber, or poPosition are not found within an skuData entity, look for these fields elsewhere in the document. Once found, insert these fields to all relevant skuData entities by populating their respective fields.
    - Do not create additional skuData entries separately for these shared attributes; instead, insert them to existing skuData entries by populating their respective fields.
    - Do not extract or associate the total Gross Weight, total Net Weight, or quantityShipped.
    """
    ci = """
    - If the containerNumber, hsCode, or poNumber are not found in the sku data, search in other location of the document and map it to all the sku entities. But do not map the total Gross Weight, Net Weight, or Quantity to all the sku entities."""  # noqa

    prompt = f"""
    Task: Fill in the following dictionary from the information in the given pdf document.

    Each data point is part of a master field called skuData. There may be multiple skuData entries in a document.
    Your goal is to extract all instances.

    Instructions:
    - Do not change the keys of the following dictionary.
    - The values should be filled in as per the schema provided below.
    - The entity can be extracted multiple times. Please pay attention to the occurrence_type.
    - Use the data field description to understand the context of the data.
    {pl if schema.name == 'skuData' else ci}

    return only the extracted data in the above format excluding all other information.
    And return the output in a valid json format.

    """.replace(
        "skuData", schema.name
    )  # Replace "skuData" with the "skus" for the CI document

    return prompt


# pylint: enable=all
async def post_processing_pl_and_ci(
    params,
    aggregated_data,
    schema_client,
    input_doc_type,
    file_content,
    processor_version,
    llm_client,
):
    """Extract the SKU data using the LLMs from the PL and CI documents.

    Args:
        params (dict): Constants stored in a dictionary
        aggregated_data (dict): The aggregated data from the document
        schema_client (object): The schema client object
        input_doc_type (str): The document type
        file_content (str): The content of the file to be processed
        processor_version (str): The version of the processor
        llm_client (object): The LLM client object

    Returns:
        dict: The aggregated data with the SKU data extracted
        str: The processor
    """
    # Get the schema from the Doc AI processor and the sku_name (i.e., "skuData" from PL & "skus" from CI)
    schema_sku, sku_name = await get_sku_doc_ai_schema(
        params, schema_client, input_doc_type
    )

    # get the schema placeholder from the Doc AI and generate the response structure
    response_schema = await generate_schema_structure(
        params, input_doc_type, schema_client
    )
    # Since we are extracting only the skuData using the LLMs
    # Extract only the 'skuData' from the response schema
    response_schema["properties"] = {
        sku_name: response_schema["properties"].pop(sku_name)
    }

    # Remove the "skuData" or "skus" key from the aggregated data if it exists
    if sku_name in aggregated_data and aggregated_data[sku_name]:
        del aggregated_data[sku_name]

    # Process the file content with the LLM to extract the SKU data
    llm_response, model_id = await process_file_w_llm(
        params, schema_sku, file_content, llm_client, response_schema
    )

    # Add the SKU result to the Doc AI aggregated data
    aggregated_data[sku_name] = llm_response[sku_name]

    # Join the LLM model id to the Doc Ai processor version
    processor_version = processor_version + "/" + model_id

    return aggregated_data, processor_version
