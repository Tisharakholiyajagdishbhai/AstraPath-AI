# 🌌 AstraPath AI - Agentic Career Navigator

AstraPath AI is an advanced, agentic career navigation platform tailored specifically for individuals aspiring to secure careers, research roles, and internships at premier space and defense organizations like **ISRO, DRDO, and NASA**. By analyzing applicant resumes and parsing complex institutional requirements, the system acts as an autonomous career strategist.

## 🌐 Live Demo
https://astrapath-ai-5z99yjk5fguavyjtycm8zb.streamlit.app/

## 🚀 Key Features

* **AI Resume Parser:** Extracts existing skills, technologies, and projects from uploaded documents using advanced NLP.
* **Skill Gap Analysis:** Semantic comparison between your current profile and targeted aerospace/defense career paths.
* **Personalized Learning Roadmaps:** Generates structured paths to acquire the technical knowledge and certifications needed.
* **Targeted Opportunities Finder:** Curates specific defense and aerospace research, internships, and entry-level positions.

## 🛠️ Tech Stack

* **Frontend/UI:** Streamlit / HTML / CSS (Python-centric interface)
* **AI & NLP:** Python (Google Gemini API / OpenAI API / LangChain / HuggingFace)
* **Data Processing:** PyPDF2 / PDFPlumber, Pandas, NumPy

## ⚙️ Installation & Local Setup

Follow these steps to set up AstraPath AI on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com
cd AstraPath-AI
```

### 2. Create a Virtual Environment
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your API keys:
```env
AI_API_KEY=your_api_key_here
```

### 5. Run the Application
```bash
streamlit run app.py
```

## 🗺️ Future Roadmap

- [ ] Integration with specific entry exam syllabi (like GATE, ISRO ICRB, DRDO SET).
- [ ] AI Mock Interview Simulator focused on Aerospace Engineering and Avionics.
- [ ] Portfolio/Project generator guidance for deep-tech domains.

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you want to add more features or fix bugs.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
