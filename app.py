import re
import streamlit as st
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="HireMatch AI", page_icon="📄", layout="wide")

st.title("🚀 HireMatch AI")
st.caption("AI-powered resume and job description compatibility analyzer")

SKILLS = [
    "python", "java", "c++", "sql", "mysql", "postgresql", "html", "css",
    "javascript", "angular", "react", "node.js", "fastapi", "flask", "django",
    "rest api", "git", "github", "docker", "aws", "azure", "machine learning",
    "deep learning", "tensorflow", "pytorch", "data structures", "dbms", "linux",
]

def has_skill(skill, text):
    pattern = r"(?<![a-z0-9])" + re.escape(skill) + r"s?(?![a-z0-9])"
    return re.search(pattern, text) is not None

resume_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description", height=250)

if resume_file and job_description:
    # Extract resume text
    reader = PdfReader(resume_file)
    resume_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text + " "

    if not resume_text.strip():
        st.error("Could not read text from this PDF. Try a text-based (not scanned) PDF.")
        st.stop()

    # Match score (TF-IDF + cosine similarity)
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, job_description])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    score = round(similarity * 100, 2)

    # Skill analysis
    resume_lower = resume_text.lower()
    job_lower = job_description.lower()
    job_skills = [s for s in SKILLS if has_skill(s, job_lower)]
    matched = [s for s in job_skills if has_skill(s, resume_lower)]
    missing = [s for s in job_skills if s not in matched]

    # Dashboard
    c1, c2, c3 = st.columns(3)
    c1.metric("Match Score", f"{score}%")
    c2.metric("Matched Skills", len(matched))
    c3.metric("Missing Skills", len(missing))

    left, right = st.columns(2)
    with left:
        st.subheader("✅ Matching Skills")
        if matched:
            for s in matched:
                st.write(f"✓ {s.title()}")
        else:
            st.write("No matching skills found.")
    with right:
        st.subheader("❌ Missing Skills")
        if missing:
            for s in missing:
                st.write(f"• {s.title()}")
        else:
            st.write("No major missing skills found.")

    st.subheader("💡 Recommendations")
    if missing:
        st.write("Consider improving these skills:")
        for s in missing:
            st.write(f"→ {s.title()}")
    else:
        st.success("Your resume contains the major skills mentioned in the job description.")