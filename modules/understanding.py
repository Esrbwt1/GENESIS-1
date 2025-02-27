# modules/understanding.py
"""
Understanding Module:
Transforms preprocessed text into semantic embeddings using a pre-trained model.
"""

from transformers import AutoTokenizer, AutoModel
import torch

def load_model(model_name="distilbert-base-uncased"):
    """
    Loads a pre-trained tokenizer and model.
    
    Args:
        model_name (str): The identifier of the pre-trained model.
        
    Returns:
        tokenizer, model: The loaded tokenizer and model.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    return tokenizer, model

def get_embeddings(text, tokenizer, model):
    """
    Converts input text into embeddings using the pre-trained model.
    
    Args:
        text (str): The input text to be transformed.
        tokenizer: The pre-trained tokenizer.
        model: The pre-trained model.
    
    Returns:
        numpy.array: A vector representing the text embedding.
    """
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze()
    return embeddings.detach().numpy()

def test_understanding_module():
    """
    Test function for the Understanding Module.
    """
    tokenizer, model = load_model()
    sample_text = "This is a sample text for the Understanding Module test."
    embeddings = get_embeddings(sample_text, tokenizer, model)
    print("Embeddings generated with shape:", embeddings.shape)

if __name__ == "__main__":
    test_understanding_module()