# modules/knowledge_graph.py
"""
Knowledge Graph Module:
Builds a simple knowledge graph to interlink concepts across domains.
Requires: networkx
Install via: pip install networkx
"""

import networkx as nx

def create_knowledge_graph():
    """
    Creates a simple knowledge graph with predefined nodes and edges.
    
    Returns:
        graph: A NetworkX graph object.
    """
    G = nx.Graph()
    # Add nodes representing concepts
    G.add_node("Artificial Intelligence")
    G.add_node("Machine Learning")
    G.add_node("Neural Networks")
    G.add_node("Reinforcement Learning")
    G.add_node("Computer Vision")
    
    # Add edges with example weights
    G.add_edge("Artificial Intelligence", "Machine Learning", weight=0.9)
    G.add_edge("Machine Learning", "Neural Networks", weight=0.8)
    G.add_edge("Neural Networks", "Reinforcement Learning", weight=0.7)
    G.add_edge("Artificial Intelligence", "Computer Vision", weight=0.85)
    
    print("[KNOWLEDGE GRAPH] Knowledge graph created with", G.number_of_nodes(), "nodes and", G.number_of_edges(), "edges.")
    return G

def query_knowledge_graph(G, concept):
    """
    Returns a list of neighboring concepts for a given concept in the knowledge graph.
    
    Args:
        G (Graph): The knowledge graph.
        concept (str): The concept to query.
        
    Returns:
        list: Neighboring concepts.
    """
    if concept in G:
        neighbors = list(G.neighbors(concept))
        print(f"[KNOWLEDGE GRAPH] Neighbors of '{concept}':", neighbors)
        return neighbors
    else:
        print(f"[KNOWLEDGE GRAPH] Concept '{concept}' not found in the graph.")
        return []

if __name__ == "__main__":
    KG = create_knowledge_graph()
    query_knowledge_graph(KG, "Machine Learning")