from datetime import datetime, timezone
from typing import Any, Dict

from pydantic import BaseModel


def pydantic_to_dynamodb(item: BaseModel) -> Dict[str, Any]:
    """
    Convert a Pydantic object to a DynamoDB-compatible dictionary.
    :param item: Pydantic model instance
    :return: DynamoDB-compatible dictionary
    """

    def serialize_value(value):
        if isinstance(value, datetime):
            return value.isoformat()  # Convert datetime to ISO 8601 string
        elif isinstance(value, list):
            return [serialize_value(v) for v in value]  # Recursively serialize lists
        elif isinstance(value, dict):
            return {k: serialize_value(v) for k, v in value.items()}  # Recursively serialize dicts
        return value  # Return as-is for other types

    return {k: serialize_value(v) for k, v in item.model_dump().items()}


def pydantic_to_appsync(item: Any) -> Any:
    """
    Recursively serialize a Pydantic object or other Python objects into a format
    compatible with AppSync, including proper datetime conversion to AWSDateTime.

    :param item: Pydantic object, list, or dict
    :return: AppSync-compatible dictionary or value
    """

    def serialize_value(value):
        if isinstance(value, datetime):
            # Convert datetime to ISO 8601 with 'Z' for UTC
            return value.astimezone(timezone.utc).isoformat()
        elif isinstance(value, BaseModel):
            # Recursively serialize Pydantic models
            return pydantic_to_appsync(value)
        elif isinstance(value, list):
            # Recursively serialize each item in a list
            return [serialize_value(v) for v in value]
        elif isinstance(value, dict):
            # Recursively serialize each key-value pair in a dictionary
            return {k: serialize_value(v) for k, v in value.items()}
        return value  # Return as-is for other types

    if isinstance(item, BaseModel):
        # Start serialization for Pydantic models
        return {k: serialize_value(v) for k, v in item.model_dump().items()}
    elif isinstance(item, list):
        # Serialize lists directly
        return [serialize_value(v) for v in item]
    elif isinstance(item, dict):
        # Serialize dictionaries directly
        return {k: serialize_value(v) for k, v in item.items()}
    else:
        # Return non-complex types as-is
        return serialize_value(item)
