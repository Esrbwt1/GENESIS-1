# main.py
"""
Full Integration of GENESIS-1 Modules:
This script demonstrates the complete data flow from text ingestion to multi-modal processing,
enhanced reasoning (using a knowledge graph), continuous learning, and long-term memory storage.
"""

from datetime import datetime
import numpy as np

# Import previous modules
from modules.perception import ingest_local_file, preprocess_text
from modules.understanding import load_model, get_embeddings
from modules.learning import evaluate_decision, update_learning_model
from modules.self_improvement import analyze_system, self_improve
from modules.memory import create_memory_event, store_memory, retrieve_memory
from modules.action import execute_action
from modules.code_analyzer import analyze_code_performance, propose_code_enhancements
from modules.auto_code_generator import generate_code_enhancement
from modules.external_data import fetch_hacker_news_headlines as fetch_headlines, preprocess_external_data
from modules.user_interface import get_user_feedback
from modules.incremental_learning import incremental_train

# Import Phase 4 modules
from modules.multi_modal import ingest_image, get_image_embedding, load_vision_model, ingest_numerical_data, preprocess_numerical_data
from modules.knowledge_graph import create_knowledge_graph, query_knowledge_graph
from modules.reasoning import enhanced_reasoning  # Use the enhanced reasoning function
from modules.long_term_memory import store_long_term_memory, retrieve_long_term_memory, query_long_term_memory

def integrate_system(text_filepath, image_path=None, csv_path=None, ci_mode=False):
    """
    Integrates all modules of GENESIS-1, including multi-modal processing, enhanced reasoning,
    and long-term memory storage.
    
    Steps:
      1. Ingest and preprocess raw text.
      2. Generate text embeddings using a pre-trained language model.
      3. Produce an enhanced reasoning decision that incorporates knowledge graph context.
      4. Evaluate the decision and update the learning model.
      5. Analyze system performance and perform self-improvement.
      6. Execute an action based on the decision.
      7. Log the event into short-term memory.
      8. Retrieve memory logs and perform code analysis.
      9. Auto-generate further code improvement suggestions.
     10. Fetch and preprocess external data.
     11. Get user feedback.
     12. Perform incremental training with new data.
     13. Process multi-modal inputs (image and numerical data) if provided.
     14. Store an event in long-term memory and query historical events.
    
    Args:
        text_filepath (str): Path to the text file.
        image_path (str, optional): Path to an image file.
        csv_path (str, optional): Path to a CSV file with numerical data.
    
    Returns:
        dict: A dictionary containing outputs and event details.
    """
    # Step 1: Ingest raw text from file and preprocess
    raw_text = ingest_local_file(text_filepath)
    tokens = preprocess_text(raw_text)
    processed_text = " ".join(tokens)
    
    # Step 2: Load language model and generate text embeddings
    tokenizer, text_model = load_model()
    text_embeddings = get_embeddings(processed_text, tokenizer, text_model)
    
    # Step 3: Produce enhanced reasoning decision (using a knowledge graph)
    decision = enhanced_reasoning(text_embeddings, concept="Machine Learning")
    
    # Step 4: Evaluate decision and update learning model
    reward = evaluate_decision(decision)
    update_learning_model(text_embeddings, decision, reward)
    
    # Step 5: Analyze system performance and trigger self-improvement
    analysis_report = analyze_system(text_embeddings, decision, reward)
    improvement_outcome = self_improve(analysis_report)
    
    # Step 6: Execute an action based on the decision
    action_outcome = execute_action(decision)
    
    # Step 7: Log the event into short-term memory
    input_summary = raw_text[:100] + "..." if len(raw_text) > 100 else raw_text
    embedding_stats = {"mean": float(np.mean(text_embeddings)), "std": float(np.std(text_embeddings))}
    memory_event = create_memory_event(
        input_summary=input_summary,
        embedding_stats=embedding_stats,
        decision=decision,
        reward=reward,
        analysis_report=analysis_report,
        improvement_outcome=improvement_outcome + " | " + action_outcome
    )
    store_memory(memory_event)
    
    # Step 8: Retrieve memory logs and perform code analysis
    memory_logs = retrieve_memory()
    code_analysis_report = analyze_code_performance(memory_logs)
    code_suggestion = propose_code_enhancements()
    auto_code_suggestion = generate_code_enhancement("The system's tokenization process is identified as a bottleneck.")
    
    print("[CODE ANALYZER] Analysis Report:", code_analysis_report)
    print("[CODE ANALYZER] Code Improvement Suggestion:", code_suggestion)
    print("[AUTO CODE GENERATOR] Code Improvement Suggestion:", auto_code_suggestion)
    
    # Step 9: Fetch external data and preprocess it
    headlines = fetch_headlines()
    external_data = preprocess_external_data(headlines)
    
    # Step 10: Get user feedback
    # Update user feedback call
    user_feedback = get_user_feedback() if not ci_mode else ""
    
    # Update file handling for CI
    if ci_mode:
        print("[CI MODE] Using test files from test_files/ directory")  
      
    # Step 11: Perform incremental training with external data and feedback
    new_training_data = external_data + " " + user_feedback
    incremental_train_success = incremental_train(new_training_data)
    
    # Step 12: Multi-modal integration: process image if provided
    image_embedding = None
    if image_path:
        image = ingest_image(image_path)
        if image:
            vision_model, vision_transform = load_vision_model()
            image_embedding = get_image_embedding(image, vision_model, vision_transform)
    
    # Step 13: Multi-modal integration: process numerical data if provided
    numerical_data = None
    if csv_path:
        df = ingest_numerical_data(csv_path)
        if df is not None:
            numerical_data = preprocess_numerical_data(df)
    
    # Step 14: Store event in long-term memory with multi-modal details
    long_term_event = {
        "timestamp": datetime.utcnow().isoformat(),
        "input_summary": input_summary,
        "decision": decision,
        "reward": reward,
        "multi_modal": {
            "image_embedding_shape": image_embedding.shape if image_embedding is not None else None,
            "numerical_data_shape": numerical_data.shape if numerical_data is not None else None
        }
    }
    store_long_term_memory(long_term_event)
    long_term_events = query_long_term_memory("Esrom")  # Example query term
    
    return {
        "text_embeddings": text_embeddings,
        "decision": decision,
        "reward": reward,
        "analysis_report": analysis_report,
        "improvement_outcome": improvement_outcome,
        "action_outcome": action_outcome,
        "memory_event": memory_event,
        "code_analysis_report": code_analysis_report,
        "code_suggestion": code_suggestion,
        "auto_code_suggestion": auto_code_suggestion,
        "external_data": external_data,
        "user_feedback": user_feedback,
        "incremental_train_success": incremental_train_success,
        "image_embedding": image_embedding,
        "numerical_data": numerical_data,
        "long_term_events": long_term_events
    }

def main(ci_mode=False):
    print("Initializing full GENESIS-1 integration with Phase 4: Multi-Domain Reasoning & Generalization...")
    
    # Define file paths (update these paths as needed)
    text_file = "sample.txt"  # Your sample text file
    image_file = "C:/Users/A3sh/Desktop/photo-1529778873920-4da4926a72c2.jpg"  # Path to your test image
    csv_file = "C:/Users/A3sh/Desktop/people-100.csv"  # Path to your numerical CSV file
    
    result = integrate_system(text_file, image_path=image_file, csv_path=csv_file, ci_mode=ci_mode)  # <── Pass CI mode to integration
    
    print("Integration complete.")
    print("Generated text embeddings with shape:", result["text_embeddings"].shape)
    print("Enhanced Reasoning Decision:", result["decision"])
    print("Reward Signal:", result["reward"])
    print("Analysis Report:", result["analysis_report"])
    print("Self-Improvement Outcome:", result["improvement_outcome"])
    print("Action Outcome:", result["action_outcome"])
    print("Short-Term Memory Event Logged:")
    print(result["memory_event"])
    print("[CODE ANALYZER] Analysis Report:", result["code_analysis_report"])
    print("[CODE ANALYZER] Code Improvement Suggestion:", result["code_suggestion"])
    print("[AUTO CODE GENERATOR] Code Improvement Suggestion:", result["auto_code_suggestion"])
    print("[EXTERNAL DATA] Preprocessed External Data:")
    print(result["external_data"])
    print("[USER FEEDBACK] Feedback Received:", result["user_feedback"])
    print("[INCREMENTAL LEARNING] Training Success:", result["incremental_train_success"])
    if result["image_embedding"] is not None:
        print("[MULTI-MODAL] Image Embedding Shape:", result["image_embedding"].shape)
    if result["numerical_data"] is not None:
        print("[MULTI-MODAL] Numerical Data Shape:", result["numerical_data"].shape)
    print("[LONG-TERM MEMORY] Queried Events:", result["long_term_events"])

if __name__ == "__main__":
    main()