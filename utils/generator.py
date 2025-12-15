import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Global warning message (used in app.py)
FALLBACK_WARNING = "⚠️ Personalized AI generation is temporarily unavailable (possible rate limit or connection issue). Please try again in a minute or two."

def generate_bullet_points(resume_text, jd_text):
    prompt = f"""You are an expert resume writer. Using ONLY the information from this person already has, create exactly 3 powerful, quantified bullet points that make their resume a perfect match for the job below.

Resume excerpt:
{resume_text[:5000]}

Job description:
{jd_text[:5000]}

Return ONLY the 3 bullet points, nothing else. Start each with a strong action verb."""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            top_p=1,
            max_tokens=300
        )
        text = response.choices[0].message.content
        lines = [line.strip(" •-*1234567890.") for line in text.split("\n") if line.strip() and not line.startswith("Note")]
        return lines[:3] if len(lines) >= 3 else lines
    except Exception as e:
        # Return only clean generic tips (warning shown separately in app.py)
        return [
            "Use strong action verbs (e.g., Developed, Optimized, Engineered, Improved) and quantified achievements with metrics",
            "Incorporate relevant keywords from the job description to improve ATS compatibility",
            "Highlight projects, experiences, and skills that directly align with the role's key requirements"
        ]

def generate_cold_email(resume_text, jd_text):
    prompt = f"""Write a short (100–140 words), confident, personalized cold email to a hiring manager for this job.

Resume summary: {resume_text[:3000]}
Job description: {jd_text[:3000]}

Tone: professional but bold, no fluff. End with clear call-to-action. Do NOT say "I came across your posting" — be direct."""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            top_p=1,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        template = """Hi [Hiring Manager's Name],

I'm reaching out because my background in [key skill/area from job description] directly aligns with your team's needs.

I've successfully [strong achievement or project relevant to the role], delivering [positive outcome or metric].

I'd appreciate 15 minutes to discuss how I can contribute to your current goals and challenges.

Available this week — looking forward to connecting.

Best regards,
[Your Name]"""
        return template