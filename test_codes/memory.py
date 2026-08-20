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