# modules/external_data.py
"""
External Data Module:
Fetches data from the internet using the Hacker News API to obtain top headlines.
Requires: requests
Install via: pip install requests
"""

import requests

def fetch_hacker_news_headlines():
    """
    Fetches the top 10 Hacker News headlines using the Hacker News API.
    
    Returns:
        list: A list of headline strings.
    """
    try:
        # Get the top story IDs from Hacker News
        top_ids_response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
        top_ids_response.raise_for_status()
        top_ids = top_ids_response.json()[:10]  # Get top 10 story IDs
        
        headlines = []
        for story_id in top_ids:
            story_response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json")
            story_response.raise_for_status()
            story = story_response.json()
            if story and "title" in story:
                headlines.append(story["title"])
        print(f"[EXTERNAL DATA] Fetched {len(headlines)} Hacker News headlines.")
        return headlines
    except Exception as e:
        print(f"[EXTERNAL DATA] Error fetching Hacker News headlines: {e}")
        return []

def preprocess_external_data(raw_data):
    """
    Preprocesses the external data by joining list items into a single string.
    
    Args:
        raw_data (list): List of strings (e.g., headlines).
        
    Returns:
        str: A single string combining the raw data.
    """
    processed = " ".join(raw_data)
    print(f"[EXTERNAL DATA] Preprocessed external data length: {len(processed)} characters.")
    return processed

if __name__ == "__main__":
    headlines = fetch_hacker_news_headlines()
    processed_data = preprocess_external_data(headlines)
    print("Processed Data:", processed_data)