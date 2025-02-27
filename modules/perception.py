# modules/perception.py
"""
Perception Module:
Handles data ingestion and preprocessing for GENESIS-1.
"""

import os
import json
import csv
import re

# For more advanced tokenization, you might later add:
# import nltk
# nltk.download('punkt')
# from nltk.tokenize import word_tokenize

def ingest_local_file(filepath):
    """
    Ingest data from a local text file.
    
    Args:
        filepath (str): Path to the text file.
        
    Returns:
        str: Content of the file.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as file:
        data = file.read()
    print(f"[INFO] Successfully ingested file: {filepath}")
    return data

def ingest_csv(filepath):
    """
    Ingest data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file.
        
    Returns:
        list: A list of rows, where each row is a dictionary (assuming headers).
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"CSV file not found: {filepath}")
    
    data = []
    with open(filepath, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    print(f"[INFO] Successfully ingested CSV: {filepath}")
    return data

def ingest_json(filepath):
    """
    Ingest data from a JSON file.
    
    Args:
        filepath (str): Path to the JSON file.
        
    Returns:
        dict or list: Parsed JSON data.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"JSON file not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
    print(f"[INFO] Successfully ingested JSON: {filepath}")
    return data

def preprocess_text(raw_text):
    """
    Preprocess the text data:
      - Lowercase conversion.
      - Remove punctuation.
      - Trim whitespace.
      - (Optionally, tokenize text.)
    
    Args:
        raw_text (str): Raw text input.
    
    Returns:
        list: List of cleaned tokens.
    """
    # Convert text to lowercase
    text = raw_text.lower()
    
    # Remove punctuation using regex
    text = re.sub(r'[^\w\s]', '', text)
    
    # Trim extra whitespace
    text = text.strip()
    
    # Simple tokenization: split by whitespace
    tokens = text.split()
    
    print(f"[INFO] Preprocessing complete. Total tokens: {len(tokens)}")
    return tokens

# Example test if module is run directly
if __name__ == "__main__":
    try:
        sample_text = ingest_local_file("sample.txt")  # Make sure to create a sample.txt file for testing
        tokens = preprocess_text(sample_text)
        print("Tokens:", tokens)
    except Exception as e:
        print(f"[ERROR] {e}")