import streamlit as st
import requests
import PyPDF2
import io

st.set_page_config(page_title="AstraPath AI", page_icon="🚀")

API_KEY = st.secrets["GROQ_API_KEY"]
st.write("API Key Loaded:", API_KEY[:10])

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def analyze_resume(resume_text):
    prompt = f"""
    You are AstraPath AI - a career agent for Space & Research aspirants (ISRO, DRDO, NASA).

    Analyze this resume and provide:
    1. ATS Score out of 100
    2. Top 5 Skills Found
    3. Skills Gap for ISRO/DRDO/Research roles
    4. Strengths of Candidate
    5. Weaknesses of Candidate
    6. Personalized Learning Roadmap (3 steps)
    7. Top 3 Job/Research roles suitable
    8. Top 3 Internships/Opportunities to apply right now

    Resume:
    {resume_text}
    """
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=data)
    st.write("Status code:", response.status_code)
     
    result = response.json()
    st.write(result)
    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    else:
        return f"Error: {result}"
# UI

st.title("🚀 AstraPath AI")
st.subheader("AI Career Agent for Space & Research Aspirants")
st.markdown("*Built for ISRO | DRDO | NASA dreamers*")

uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf")
job_description = st.text_area("Paste Job Description (Optional)")

if uploaded_file:
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
    resume_text = ""
    for page in pdf_reader.pages:
        resume_text += page.extract_text()

    st.success("✅ Resume uploaded successfully!")

    if st.button("🚀 Analyze My Career Path"):
        with st.spinner("AstraPath AI is analyzing your resume..."):
            analysis = analyze_resume(resume_text)
        st.markdown("## Your Career Analysis")
        st.markdown(analysis)
        st.balloons()
