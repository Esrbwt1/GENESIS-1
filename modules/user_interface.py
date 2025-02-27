# modules/user_interface.py
"""
User Interaction Module:
Provides a simple command-line interface for users to give feedback.
"""

def get_user_feedback():
    """
    Prompts the user for feedback regarding the system's decision.
    
    Returns:
        str: The feedback input by the user.
    """
    feedback = input("Enter your feedback on the system's decision (or type 'none' to skip): ")
    if feedback.strip().lower() == "none":
        print("[USER INTERFACE] No feedback provided.")
        return ""
    else:
        print(f"[USER INTERFACE] Feedback received: {feedback}")
        return feedback