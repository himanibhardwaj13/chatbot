from typing import Any, TypedDict

class SQLState(TypedDict):
    """A dictionary that represents the state of a SQL query."""

    question: str
    relevant_examples: list[str]
    relevant_schema: list[str]
    prompt: str
    sql: str
    data: list[dict]
    response: dict[str, Any]