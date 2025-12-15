# ResumeMatch AI 🤖

**Live Link**: https://resumematch-ai.streamlit.app/

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

### 📸 Screenshots
<img width="1913" height="907" alt="resumematch_ai Screenshot_01" src="https://github.com/user-attachments/assets/7eb26f7d-6056-42b8-8041-39aa075dcece" />
<img width="1897" height="911" alt="resumematch_ai Screenshot_02" src="https://github.com/user-attachments/assets/abd103ed-87ee-461d-b67c-070140da158c" />
