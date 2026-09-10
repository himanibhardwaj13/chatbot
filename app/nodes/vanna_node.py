from app.graph.state import SQLState
from app.services.vanna_service import vanna_service

  # Initialize with your Vanna instance

def vanna_node(state:SQLState):
    """
    This function represents a node in the graph that processes the state and returns a response.
    It can be used to handle specific logic based on the current state of the conversation.
    
    Args:
        state: The current state of the conversation.) 
    """
    question = state.get("question")
    response = vanna_service.retrieve(question)
    
    return {
        "relevant_examples": response["relevant_examples"],
        "relevant_schema": response["relevant_schema"]
    }
