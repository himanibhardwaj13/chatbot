from app.graph.state import SQLState

def response_formatter_node(state: SQLState):
    """
    Formats the response string by removing any leading or trailing whitespace.

    Args:
        response (str): The response string to be formatted.
    """
    rows= state.get("data")
    return {
        "response": {
            "type": "table",
            "items": rows
        }
    }