# 🚀 HireMatch AI

An AI-powered resume and job description compatibility analyzer.

## 🎯 Problem
Candidates often apply without knowing how well their resume matches a job description. HireMatch AI gives a match score and a skill-gap analysis.

## ✨ Features
- Resume PDF upload
- Resume–JD similarity score
- Matching and missing skill detection
- Improvement recommendations
- Interactive dashboard

## 🛠️ Tech Stack
Python, Streamlit, Scikit-learn, PyPDF, TF-IDF, Cosine Similarity

## ⚙️ How It Works
Resume PDF → Text Extraction → TF-IDF → Cosine Similarity → Match Score → Skill Gap Analysis

## 🚀 Installation
```bash
git clone https://github.com/Nasira910/hirematch-ai.git
cd hirematch-ai
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## 📸 Screenshots
![Results](screenshot1.png)

## 🔮 Future Enhancements
- ATS score
- Downloadable PDF report
- LLM-based resume feedback

## 👩‍💻 Author
Nasira
