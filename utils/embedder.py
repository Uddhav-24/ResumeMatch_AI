from sentence_transformers import SentenceTransformer
import chromadb

# Load model and initialize ChromaDB client
model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path="../chroma_db")
collection = client.get_or_create_collection("resume_jd")

def get_embeddings(texts):
    return model.encode(texts, show_progress_bar=False)