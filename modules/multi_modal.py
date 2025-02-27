# modules/multi_modal.py
"""
Multi-Modal Module:
Extends perception to handle images and numerical data.
Requires: Pillow, torchvision, pandas, numpy
Install via: pip install pillow torchvision pandas numpy
"""

from PIL import Image
import torch
import torchvision.transforms as transforms
import pandas as pd
import numpy as np
from torchvision import models
import torch.nn as nn

def load_vision_model():
    """
    Loads a pre-trained ResNet18 model and removes the final classification layer to extract embeddings.
    
    Returns:
        model: The modified ResNet18 model.
        transform: The preprocessing transform.
    """
    model = models.resnet18(pretrained=True)
    # Remove the final fully-connected layer to extract embeddings
    model = nn.Sequential(*list(model.children())[:-1])
    model.eval()  # Set to evaluation mode
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
    return model, transform

def ingest_image(file_path):
    """
    Loads an image from the given file path.
    
    Args:
        file_path (str): Path to the image file.
        
    Returns:
        image: A PIL Image.
    """
    try:
        image = Image.open(file_path).convert("RGB")
        print(f"[MULTI-MODAL] Successfully ingested image: {file_path}")
        return image
    except Exception as e:
        print(f"[MULTI-MODAL] Error loading image: {e}")
        return None

def get_image_embedding(image, model, transform):
    """
    Processes an image and returns its embedding using the vision model.
    
    Args:
        image (PIL.Image): Input image.
        model: Pre-trained vision model.
        transform: Preprocessing transform.
        
    Returns:
        numpy.array: Image embedding vector.
    """
    input_tensor = transform(image).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        embedding = model(input_tensor)
    # Flatten the embedding tensor and convert to numpy array
    embedding = embedding.view(embedding.size(0), -1).squeeze().numpy()
    print(f"[MULTI-MODAL] Image embedding generated with shape: {embedding.shape}")
    return embedding

def ingest_numerical_data(csv_path):
    """
    Loads numerical data from a CSV file into a pandas DataFrame.
    
    Args:
        csv_path (str): Path to the CSV file.
        
    Returns:
        DataFrame: The loaded numerical data.
    """
    try:
        df = pd.read_csv(csv_path)
        print(f"[MULTI-MODAL] Successfully ingested numerical data from: {csv_path}")
        return df
    except Exception as e:
        print(f"[MULTI-MODAL] Error loading CSV data: {e}")
        return None

def preprocess_numerical_data(df):
    """
    Preprocesses numerical data by normalizing each numeric column.
    
    Args:
        df (DataFrame): Input numerical data.
        
    Returns:
        numpy.array: Processed data as an array.
    """
    numeric = df.select_dtypes(include=[np.number])
    normalized = (numeric - numeric.mean()) / numeric.std()
    processed = normalized.to_numpy()
    print(f"[MULTI-MODAL] Preprocessed numerical data with shape: {processed.shape}")
    return processed

if __name__ == "__main__":
    # For testing purposes, replace file paths with valid ones if available
    # Test image ingestion (replace 'path_to_image.jpg' with an actual image file path)
    image = ingest_image("C:/Users/A3sh/Desktop/photo-1529778873920-4da4926a72c2.jpg")
    if image:
        model, transform = load_vision_model()
        _ = get_image_embedding(image, model, transform)
    
    # Test numerical data ingestion (replace 'data.csv' with a valid CSV file path)
    df = ingest_numerical_data("C:/Users/A3sh/Desktop/people-100.csv")
    if df is not None:
        _ = preprocess_numerical_data(df)