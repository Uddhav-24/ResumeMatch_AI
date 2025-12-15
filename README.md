# ResumeMatch AI 🤖

**Live Demo**: https://resumematch-ai.streamlit.app/

An AI-powered tool that instantly matches your resume to any job description and generates:
- Match score (semantic similarity)
- 3 tailored bullet points to strengthen your resume
- Personalized cold email ready to send
- Full downloadable application kit (.txt & .md)

### 🚀 Features
- Semantic match score using sentence embeddings
- Instant personalized bullets & cold email via Groq Llama-3.3-70B
- Graceful fallback with generic tips if AI is temporarily unavailable
- One-click download of full application kit
- Fully open-source and free to use

### 🛠 Tech Stack
- **Frontend**: Streamlit
- **AI**: Groq Llama-3.3-70B + sentence-transformers (all-MiniLM-L6-v2)
- **Backend**: Python, ChromaDB for vector storage
- **Deployment**: Streamlit Community Cloud

### 📸 Screenshot
