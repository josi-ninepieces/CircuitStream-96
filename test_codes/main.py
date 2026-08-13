import chromadb
import chromadb.utils.embedding_functions as ef
import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

db = chromadb.PersistentClient(path="../chroma_db")
memories = db.get_or_create_collection("my_facts")

def add_memory(memories, added_doc):
    memories.upsert(
        documents=[ added_doc,
        ],
        ids=[f"fact{memories.count()+1}"], # The documents are stored as ids.
    )

print("/nstored:", memories.count(), "my_facts")

question = str(input("What question do you have? \n ")) #<-Replace with a user input in the terminal

results = memories.query(query_texts=[question], n_results=2)
notes = "\n".join(results["documents"][0])

prompt = f"Using these notes: {notes}, answer the question below: {question}"

client = OpenAI(
base_url="https://api.groq.com/openai/v1",
api_key=os.getenv("GITHUB_TOKEN"),
)
r = client.chat.completions.create(
model="llama-3.3-70b-versatile",
messages=[{"role": "user", "content": prompt}],
)
add_memory(memories, rf"Previous conversation's Question: {question} \nAnswer: {r.choices[0].message.content}")
# print(r)    # uncomment to see the whole messy response
print("Ai response")
print(r.choices[0].message.content)