from app.services.sql_validation_service import sql_validation_service
from chatbot.app.graph.state import SQLState

def sql_validation_node(state: SQLState):
    """
    This function takes a SQLState object as input and returns a dictionary containing the response data.

    Args:
        state (SQLState): The SQLState object containing the response data.
    """
    sql = state.get("sql")
    validated_sql = sql_validation_service.validate(sql)

    return {"sql": validated_sql}