from app.graph.state import SQLState
from app.services.gemini_service import gemini_service

def gemini_node(state: SQLState):
    """
    This function takes a SQLState object as input and returns a dictionary containing the response data.

    Args:
        state (SQLState): The SQLState object containing the response data.
    """
    question = state.get("question")
    examples = state.get("relevant_examples", [])
    schema = state.get("relevant_schema", [])

    sql = gemini_service.generate_sql(question, examples, schema)

    return {"sql": sql} 