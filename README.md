
# 🚀 AstraPath AI — AI Career Agent for Space & Research Aspirants

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LLM](https://img.shields.io/badge/LLM-Powered-7C3AED?style=for-the-badge&logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)

**Built for ISRO · DRDO · NASA dreamers**

[🌐 Live Demo](https://astrapath-ai-5z99yjk5fguavyjtycm8zb.streamlit.app/) · [📬 Contact](mailto:tisharakholiya19@gmail.com)

</div>

---

## 🌟 What is AstraPath AI?

AstraPath AI is an **AI-powered career agent** that analyzes your resume and generates a **personalized career roadmap** for students aspiring to work in Space, Research, and AI organizations like ISRO, DRDO, and NASA.

Just upload your resume — and the AI does the rest.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📊 **ATS Score Analysis** | AI evaluates your resume on 5 dimensions — formatting, skills, projects, education, keywords |
| 🔍 **Skill Gap Analysis** | Identifies missing skills for ISRO / DRDO / AI / Research roles — High, Medium & Low priority |
| 🗺️ **Career Roadmap** | Personalized 3-month, 6-month & 12-month action plan |
| 💼 **Best Career Roles** | Suggests roles best suited to your profile |
| 📚 **Course Recommendations** | Recommends specific courses with platform, duration & difficulty |
| 🛠️ **Project Suggestions** | Gives you real project ideas aligned with your target domain |
| 🎯 **Recruiter Feedback** | Final rating on Overall Profile, Interview Readiness & Research Readiness |

---

## 🛠️ Tech Stack

```
📄 PDF Parsing       →  pdfplumber / PyPDF2
🧠 AI Analysis       →  LLM API (Prompt Engineering)
🌐 Frontend          →  Streamlit
☁️  Deployment       →  Streamlit Community Cloud
🐍 Language          →  Python 3.10+
```

---

## ⚙️ How It Works

```
User uploads Resume (PDF)
        ↓
PDF text extracted using pdfplumber
        ↓
Optional: Job Description pasted by user
        ↓
Structured prompt sent to LLM API
        ↓
AI returns JSON with ATS score, skill gaps,
roadmap, courses, projects, feedback
        ↓
Results displayed on Streamlit UI
```

---

## 🚀 Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/astrapath-ai.git
cd astrapath-ai
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
Create a `.env` file:
```
LLM_API_KEY=your_api_key_here
```

### 4. Run the app
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
astrapath-ai/
├── app.py                  # Main Streamlit app
├── utils/
│   ├── pdf_parser.py       # PDF text extraction
│   ├── prompt_builder.py   # LLM prompt construction
│   └── response_parser.py  # Parse AI response to UI
├── requirements.txt
├── .env.example
└── README.md
```

---

## 📸 Demo

> Upload your resume → Get instant AI-powered career analysis

🔗 **[Try it live here](https://astrapath-ai-5z99yjk5fguavyjtycm8zb.streamlit.app/)**

---

## 🎯 Target Audience

- 🚀 Students aspiring for **ISRO / DRDO / NASA** careers
- 🤖 Undergrads in **CSE, AI/ML, Data Science**
- 🔬 Anyone targeting **Research or Space Technology** roles

---

## 🙋‍♀️ About the Developer

**Tisha Rakholiya**
B.Tech CSE (AI & Data Science) · ITM SLS University, Vadodara
CodeCrafters C++ Global Rank **#199**

📧 tisharakholiya19@gmail.com
🔗 [LinkedIn](https://linkedin.com) · [GitHub](https://github.com)

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">
Made with ☕ + 🤖 by Tisha Rakholiya
</div>
