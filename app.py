import streamlit as st
from utils.parser import extract_text_from_pdf
from utils.matcher import calculate_match_score
from utils.generator import generate_bullet_points, generate_cold_email

# ====================== PAGE CONFIG & STYLE ======================
st.set_page_config(
    page_title="ResumeMatch AI",
    page_icon="Robot",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main {background-color: #0e1117; color: white;}
    .stButton>button {background-color: #1e90ff; color: white; border: none; border-radius: 8px; height: 3em;}
    .stDownloadButton>button {background-color: #ff3366; color: white; border: none; border-radius: 8px;}
    h1, h2, h3 {color: #00ffaa !important;}
</style>
""", unsafe_allow_html=True)

# ====================== SIDEBAR ======================
with st.sidebar:
    st.markdown("# ResumeMatch AI")
    st.markdown("**Instant JD matching + application kit**")
    st.divider()
    st.markdown("Made by **Uddhav Davey**")
    st.markdown("[GitHub](https://github.com/Uddhav-24) • [LinkedIn](https://www.linkedin.com/in/uddhavdavey/) • [Substack](https://substack.com/@uddhavdavey/posts)")

# ====================== MAIN UI ======================
st.title("ResumeMatch AI")
st.markdown("### Upload your resume + paste any job description → get your full application kit in seconds")

col1, col2 = st.columns([1, 1])
with col1:
    resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
with col2:
    jd_text = st.text_area("Paste Job Description", height=220, placeholder="Ctrl+V from LinkedIn / Wellfound...")

if st.button("Analyze Match & Generate Kit", type="primary", use_container_width=True):
    if not resume_file:
        st.error("Please upload your resume PDF")
    elif not jd_text.strip():
        st.error("Please paste a job description")
    else:
        with st.spinner("Reading resume..."):
            resume_text = extract_text_from_pdf(resume_file)

        with st.spinner("Calculating match score..."):
            score, details = calculate_match_score(resume_text, jd_text)

        st.markdown("---")
        col_a, col_b = st.columns([1, 3])
        with col_a:
            st.markdown(f"<h1 style='text-align:center; color:#00ffaa'>{score:.1f}%</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align:center; font-size:18px'>Match Score</p>", unsafe_allow_html=True)
        with col_b:
            if score >= 80:
                st.success("Excellent fit — apply with confidence!")
            elif score >= 60:
                st.info("Strong match — minor tailoring needed")
            else:
                st.warning("Needs improvement — use the bullets below")

        st.progress(score / 100)

        # ========= BULLET POINTS =========
        st.subheader("3 Tailored Bullet Points")
        bullets = generate_bullet_points(resume_text, jd_text)

        # Show warning only once if in fallback mode
        is_fallback = any("strong action verbs" in b.lower() or "ats compatibility" in b.lower() for b in bullets)
        if is_fallback:
            st.warning("Personalized AI generation is temporarily unavailable (rate limit or connection issue). "
                       "Please try again in a minute or two. Generic tips shown below.")

        for i, bullet in enumerate(bullets, 1):
            st.markdown(f"**{i}.** {bullet}")

        # ========= COLD EMAIL =========
        st.subheader("Personalized Cold Email")
        email = generate_cold_email(resume_text, jd_text)

        if "hi [hiring manager" in email.lower():
            st.warning("Personalized AI generation is temporarily unavailable. Generic template shown below.")

        st.text_area("Copy & customize → send on LinkedIn or email", email, height=320)

        # ========= DOWNLOAD KIT =========
        st.markdown("### Download Your Full Application Kit")
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            st.download_button(
                label="Download Everything (.txt)",
                data=f"Match Score: {score:.1f}%\n\nBullets:\n" + "\n".join([f"• {b}" for b in bullets]) + f"\n\nCold Email:\n\n{email}",
                file_name="ResumeMatch_Application_Kit.txt",
                mime="text/plain"
            )
        with col_d2:
            st.download_button(
                label="Download Full Report (.md)",
                data=f"# ResumeMatch AI Report\n\n**Score**: {score:.1f}%\n\n## Bullets\n" + "\n".join([f"- {b}" for b in bullets]) + f"\n\n## Cold Email\n\n{email}",
                file_name="ResumeMatch_Report.md",
                mime="text/markdown"
            )

        st.success("Done! Your complete application kit is ready.")
        st.balloons()

# ====================== FOOTER ======================
st.markdown("---")
st.caption("Powered by Groq Llama-3.3-70B • Free & open-source")