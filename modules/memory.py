# modules/memory.py
"""
Memory Module:
Stores and retrieves past events for GENESIS-1.
This module enables persistent logging of interactions, decisions, and self-improvement data.
"""

import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"

def initialize_memory():
    """
    Initializes the memory storage file if it doesn't exist.
    """
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
        print("[MEMORY] Initialized new memory storage.")
    else:
        print("[MEMORY] Memory storage already exists.")

def store_memory(event):
    """
    Appends a new memory event to the memory storage file.
    
    Args:
        event (dict): A dictionary containing event data.
    """
    initialize_memory()
    # Read the existing memory
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        memory = json.load(f)
    
    # Append the new event
    memory.append(event)
    
    # Write the updated memory back to the file
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4)
    
    print("[MEMORY] Event stored successfully.")

def retrieve_memory():
    """
    Retrieves all memory events from the memory storage file.
    
    Returns:
        list: A list of memory events (each event is a dictionary).
    """
    initialize_memory()
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        memory = json.load(f)
    return memory

def create_memory_event(input_summary, embedding_stats, decision, reward, analysis_report, improvement_outcome):
    """
    Creates a memory event with a timestamp and provided data.
    
    Args:
        input_summary (str): A brief summary of the raw input.
        embedding_stats (dict): Summary statistics of the embeddings (e.g., mean, std).
        decision (str): The reasoning decision.
        reward (int): The reward signal.
        analysis_report (dict): The analysis report from the Self-Improvement Module.
        improvement_outcome (str): Outcome message from self-improvement.
    
    Returns:
        dict: A memory event dictionary.
    """
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "input_summary": input_summary,
        "embedding_stats": embedding_stats,
        "decision": decision,
        "reward": reward,
        "analysis_report": analysis_report,
        "improvement_outcome": improvement_outcome
    }
    return event

def test_memory_module():
    """
    Test function for the Memory Module.
    """
    # Create a dummy memory event
    dummy_event = create_memory_event(
        input_summary="This is a sample text for testing.",
        embedding_stats={"mean": 0.123, "std": 0.456},
        decision="Positive inference: The context is positive.",
        reward=1,
        analysis_report={"average_embedding_value": 0.123, "improvement_needed": False},
        improvement_outcome="No self-improvement required."
    )
    
    # Store the dummy event
    store_memory(dummy_event)
    
    # Retrieve and print all memory events
    memory = retrieve_memory()
    print("[MEMORY] Retrieved events:")
    for event in memory:
        print(event)

if __name__ == "__main__":
    test_memory_module()