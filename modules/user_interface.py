# modules/user_interface.py
"""
User Interaction Module:
Provides a simple command-line interface for users to give feedback.
Handles CI environments where interactive input is not available.
"""

import os

def get_user_feedback():
    """
    Prompts the user for feedback regarding the system's decision.
    Automatically skips input in CI environments.
    
    Returns:
        str: The feedback input by the user, or empty string in CI.
    """
    if os.environ.get('CI') == 'true':
        print("[USER INTERFACE] Running in CI mode - skipping feedback")
        return ""
    
    try:
        feedback = input("Enter your feedback on the system's decision (or type 'none' to skip): ")
    except EOFError:
        print("[USER INTERFACE] No input available - proceeding without feedback")
        return ""
        
    if feedback.strip().lower() == "none":
        print("[USER INTERFACE] No feedback provided.")
        return ""
        
    print(f"[USER INTERFACE] Feedback received: {feedback}")
    return feedback