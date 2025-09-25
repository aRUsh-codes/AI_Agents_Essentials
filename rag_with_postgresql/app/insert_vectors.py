from datetime import datetime

import pandas as pd
from database.vector_store import VectorStore
from timescale_vector.client import uuid_from_time
import time
from openai._exceptions import RateLimitError

# Initialize VectorStore
vec = VectorStore()

# Read the CSV file
df = pd.read_csv("../data/faq_dataset.csv", sep=";")


# Prepare data for insertion
def prepare_record(row):
    """Prepare a record for insertion into the vector store with rate limit handling."""
    content = f"Question: {row['question']}\nAnswer: {row['answer']}"
    
    # Retry logic for rate limits
    retries = 5
    delay = 1  # initial delay in seconds
    while retries > 0:
        try:
            embedding = vec.get_embedding(content)
            break
        except RateLimitError:
            print(f"Rate limit hit, retrying in {delay} seconds...")
            time.sleep(delay)
            delay *= 2  # exponential backoff
            retries -= 1
    else:
        # If all retries fail, raise an exception
        raise Exception("Failed to get embedding after multiple retries due to rate limits.")

    return pd.Series(
        {
            "id": str(uuid_from_time(datetime.now())),
            "metadata": {
                "category": row["category"],
                "created_at": datetime.now().isoformat(),
            },
            "contents": content,
            "embedding": embedding,
        }
    )

# Apply to your dataframe
records_df = df.apply(prepare_record, axis=1)

# Create tables and insert data
vec.create_tables()
vec.create_index()  # DiskAnnIndex
vec.upsert(records_df)