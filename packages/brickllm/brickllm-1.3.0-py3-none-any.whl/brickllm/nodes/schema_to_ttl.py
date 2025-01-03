import json
from typing import Any, Dict

from langchain_core.messages import HumanMessage, SystemMessage

from .. import State, TTLSchema
from ..helpers import schema_to_ttl_instructions, ttl_example
from ..logger import custom_logger


def schema_to_ttl(state: State, config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate a TTL (Turtle) script from the building description and component hierarchy.

    Args:
        state (State): The current state containing the user prompt, sensors, and element hierarchy.
        config (dict): Configuration dictionary containing the language model.

    Returns:
        dict: A dictionary containing the generated TTL output.
    """
    custom_logger.eurac("📝 Generating TTL from schema")

    user_prompt = state["user_prompt"]
    try:
        sensors_dict = state["uuid_list"]
    except KeyError:
        sensors_dict = []
    elem_hierarchy = state["elem_hierarchy"]

    # sensors_dict_json = json.dumps(sensors_dict, indent=2)
    elem_hierarchy_json = json.dumps(elem_hierarchy, indent=2)

    # Get the model name from the config
    llm = config.get("configurable", {}).get("llm_model")

    # Enforce structured output
    structured_llm = llm.with_structured_output(TTLSchema)

    # System message
    system_message = schema_to_ttl_instructions.format(
        prompt=user_prompt,
        uuid_list=sensors_dict,
        elem_hierarchy=elem_hierarchy_json,
        ttl_example=ttl_example,
    )

    # Generate question
    answer = structured_llm.invoke(
        [SystemMessage(content=system_message)]
        + [HumanMessage(content="Generate the TTL.")]
    )

    return {"ttl_output": answer.ttl_output}
