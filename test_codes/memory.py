import chromadb
import chromadb.utils.embedding_functions as ef

db = chromadb.PersistentClient(path="../chroma_db")
memories = db.get_or_create_collection("my_facts")

# <<< CHANGE THESE TO THREE FACTS ABOUT YOU >>>
memories.upsert(
    documents=[
        "I love learning about technology",
        "I play music and many instruments",
        "I live in Canada"
    ],
    ids=["fact1", "fact2", "fact3"], # The documents are stored as ids.
)

print("/nstored:", memories.count(), "facts")

question = "Facts"
results = memories.query(query_texts=[question], n_results=4)
print(results["documents"], results["distances"])

import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI(
base_url="https://api.groq.com/openai/v1",
api_key=os.getenv("GITHUB_TOKEN"),
)
r = client.chat.completions.create(
model="llama-3.3-70b-versatile",
messages=[{"role": "user", "content": "what is my name?"}],
)
# print(r)    # uncomment to see the whole messy response
print(r.choices[0].message.content)