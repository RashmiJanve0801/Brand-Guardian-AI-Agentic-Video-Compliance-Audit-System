from langgraph.graph import START, StateGraph, END
from backend.src.graph.state import VideoAuditState
from backend.src.graph.nodes import index_video_node, audit_content_node

def create_graph():
    '''
    Constructs and compiles the Langgraph workflow
    Returns :
    Compiled Graph : runnable graph object for execution
    '''
    # Initialize the graph with state schema 
    workflow = StateGraph(VideoAuditState)

    # Add the nodes 
    workflow.add_node("video_indexer", index_video_node)
    workflow.add_node("content_auditor", audit_content_node)

    # Define the edges
    workflow.add_edge(START, "video_indexer")
    workflow.add_edge("video_indexer", "content_auditor")
    workflow.add_edge("content_auditor", END)

    # Compile the graph
    app = workflow.compile()
    return app

app = create_graph()
