# modules/reasoning.py
"""
Reasoning Module:
Enhanced reasoning that now can incorporate knowledge graph queries.
"""

import numpy as np
from modules.knowledge_graph import create_knowledge_graph, query_knowledge_graph

def simple_reasoning(embeddings):
    """
    Original simple reasoning function using embeddings.
    
    Args:
        embeddings (numpy.array): Semantic embeddings.
        
    Returns:
        str: A reasoning decision.
    """
    mean_value = np.mean(embeddings)
    if mean_value > 0:
        decision = "Positive inference: The input context is interpreted as positive."
    else:
        decision = "Negative inference: The input context is interpreted as negative."
    return decision

def enhanced_reasoning(embeddings, concept="Machine Learning"):
    """
    Enhanced reasoning that queries a knowledge graph to enrich the decision.
    
    Args:
        embeddings (numpy.array): Semantic embeddings.
        concept (str): A concept to query in the knowledge graph.
        
    Returns:
        str: An enriched reasoning decision.
    """
    basic_decision = simple_reasoning(embeddings)
    KG = create_knowledge_graph()
    related_concepts = query_knowledge_graph(KG, concept)
    decision = f"{basic_decision} Additionally, related concepts for '{concept}' are: {related_concepts}."
    return decision

if __name__ == "__main__":
    dummy_embeddings = np.random.randn(768)
    print("Simple Reasoning:", simple_reasoning(dummy_embeddings))
    print("Enhanced Reasoning:", enhanced_reasoning(dummy_embeddings))