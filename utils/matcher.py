from .embedder import get_embeddings, collection
import numpy as np

def chunk_text(text, chunk_size=300):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def calculate_match_score(resume_text, jd_text):
    resume_chunks = chunk_text(resume_text)
    jd_chunks = chunk_text(jd_text)
    
    resume_emb = get_embeddings(resume_chunks)
    jd_emb = get_embeddings(jd_chunks)
    
    # Simple cosine similarity
    similarities = np.dot(resume_emb, jd_emb.T)
    similarities = similarities.flatten()
    
    score = float(np.mean(similarities) * 100)
    
    details = {
        "Resume chunks": len(resume_chunks),
        "JD chunks": len(jd_chunks),
        "Average similarity": round(float(np.mean(similarities)), 3),
        "Final score": round(score, 1)
    }
    
    return score, details