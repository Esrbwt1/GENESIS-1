# distributed_processing.py
import multiprocessing
from modules.external_data import fetch_hacker_news_headlines, preprocess_external_data

def process_external_data(_):
    headlines = fetch_hacker_news_headlines()
    processed = preprocess_external_data(headlines)
    return processed

if __name__ == "__main__":
    # Create a pool with 2 processes as an example
    pool = multiprocessing.Pool(processes=2)
    results = pool.map(process_external_data, range(2))
    pool.close()
    pool.join()
    print("Distributed processing results:", results)