from app.graph.state import SQLState
from app.services.database_service import database_service

def database_node(state: SQLState):
    """
    This function takes a SQLState object as input and returns a dictionary containing the response data.

    Args:
        state (SQLState): The SQLState object containing the response data.
    """
    sql = state.get("sql")
    rows = database_service.execute(sql)

    return {
        "data": rows,
    }