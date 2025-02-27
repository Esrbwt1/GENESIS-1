# modules/long_term_memory.py
"""
Long-Term Memory Module:
Extends the memory system to support long-term storage and retrieval of historical events.
"""

import json
import os
from datetime import datetime

LONG_TERM_MEMORY_FILE = "long_term_memory.json"

def initialize_long_term_memory():
    """
    Initializes the long-term memory storage file if it doesn't exist.
    """
    if not os.path.exists(LONG_TERM_MEMORY_FILE):
        with open(LONG_TERM_MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
        print("[LONG-TERM MEMORY] Initialized new long-term memory storage.")
    else:
        print("[LONG-TERM MEMORY] Long-term memory storage already exists.")

def store_long_term_memory(event):
    """
    Appends a new event to the long-term memory storage.
    
    Args:
        event (dict): A memory event.
    """
    initialize_long_term_memory()
    with open(LONG_TERM_MEMORY_FILE, "r", encoding="utf-8") as f:
        memory = json.load(f)
    memory.append(event)
    with open(LONG_TERM_MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4)
    print("[LONG-TERM MEMORY] Event stored successfully.")

def retrieve_long_term_memory():
    """
    Retrieves all events from long-term memory.
    
    Returns:
        list: A list of memory events.
    """
    initialize_long_term_memory()
    with open(LONG_TERM_MEMORY_FILE, "r", encoding="utf-8") as f:
        memory = json.load(f)
    return memory

def query_long_term_memory(query_term):
    """
    Searches long-term memory for events that contain the query term in the input summary.
    
    Args:
        query_term (str): Term to search for.
        
    Returns:
        list: Matching memory events.
    """
    memory = retrieve_long_term_memory()
    results = [event for event in memory if query_term.lower() in event.get("input_summary", "").lower()]
    print(f"[LONG-TERM MEMORY] Found {len(results)} events matching '{query_term}'.")
    return results

if __name__ == "__main__":
    # Test storing a dummy event
    dummy_event = {
        "timestamp": datetime.utcnow().isoformat(),
        "input_summary": "Test event for long-term memory.",
        "decision": "Test decision",
        "reward": 1
    }
    store_long_term_memory(dummy_event)
    print("All long-term memory events:", retrieve_long_term_memory())
    query_long_term_memory("test")