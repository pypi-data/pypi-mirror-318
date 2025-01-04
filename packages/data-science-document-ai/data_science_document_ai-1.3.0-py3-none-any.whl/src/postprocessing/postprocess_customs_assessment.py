"""Postprocessing for customs assessment."""
from src.postprocessing.common import remove_none_values


def combine_customs_assessment_results(doc_ai, llm):
    """
    Combine results from DocAI and LLM extractions.

    Args:
        doc_ai: result from DocAI
        llm: result from LLM

    Returns:
        combined result
    """
    result = doc_ai.copy()
    llm = remove_none_values(llm)
    if not llm:
        return result
    for key in llm.keys():
        if key not in result:
            result[key] = llm[key]
    if "containers" in llm.keys():
        if len(llm["containers"]) < len(result["containers"]):
            result["containers"] = llm["containers"]
        else:
            for i in range(len(llm["containers"])):
                if i == len(result["containers"]):
                    result["containers"].append(llm["containers"][i])
                else:
                    for key in llm["containers"][i].keys():
                        result["containers"][i][key] = llm["containers"][i][key]
    return result
