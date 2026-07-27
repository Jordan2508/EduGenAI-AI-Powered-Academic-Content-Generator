# 📚 EduGenAI – Intelligent Academic Content Generator

EduGenAI is a Generative AI-powered web application that helps students, educators, and professionals generate high-quality academic content instantly. With just a few inputs such as topic, language, content type, tone, education level, and desired length, users can generate well-structured educational content in a single click.

EduGenAI extends the concept to the education domain by focusing on academic writing and learning assistance.

---

# ✨ Features

- 📝 Generate academic content on any topic
- 🌍 Supports multiple languages (English & Hinglish)
- 📏 Choose content length
  - Short
  - Medium
  - Long
- 📚 Multiple Content Types
  - Assignment
  - Essay
  - Notes
  - Blog
  - Research Article
  - Speech
- 🎯 Multiple Writing Tones
  - Academic
  - Formal
  - Professional
  - Friendly
  - Casual
  - Creative
- 🎓 Select Education Level
  - School
  - High School
  - College
  - Undergraduate
  - Graduate
- ⚡ AI-generated content using Groq LLM
- 📄 Download generated content as PDF
- 📝 Download generated content as DOCX
- 🎨 Clean and user-friendly Streamlit interface
- ☁️ Deployed on Render

---

# 💡 Problem Statement

Students often spend a significant amount of time writing assignments, notes, essays, speeches, and research content. Existing AI writing tools are generally designed for broad use cases and do not specifically target educational needs.

EduGenAI simplifies this process by allowing users to generate customized academic content tailored to their preferred language, education level, writing style, and format within seconds.

---

# ⚙️ Tech Stack

## Frontend

- Streamlit

## Backend

- Python

## AI & LLM

- LangChain
- Groq API
- GPT-OSS-120B Model

## Libraries

- python-dotenv
- python-docx
- reportlab

## Deployment

- Render

---

# 📂 Project Structure

```
EduGenAI/
│
├── main.py
├── post_generator.py
├── openai_helper.py
├── utils.py
├── requirements.txt
├── runtime.txt
├── README.md
└── .streamlit/
      └── config.toml
```

---

# 🖥️ Application Workflow

```
User Inputs

      ↓

Enter Topic

      ↓

Choose Language

      ↓

Select Length

      ↓

Choose Content Type

      ↓

Select Tone

      ↓

Select Education Level

      ↓

Click Generate

      ↓

Groq LLM Generates Content

      ↓

Display Generated Content

      ↓

Download as PDF or DOCX
```

---

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a **.env** file

```
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Run the application

```bash
streamlit run main.py

---

# 🎯 Learning Outcomes

Through this project, I gained hands-on experience with:

- Prompt Engineering
- Large Language Models (LLMs)
- LangChain Framework
- Groq API Integration
- Streamlit Web Application Development
- Environment Variable Management
- PDF & DOCX Generation
- Deploying AI Applications on Render
- Python Project Structuring
- Building End-to-End GenAI Applications

---

## ⭐ If you found this project useful, don't forget to Star the repository!

```
⭐ Star this repository
🍴 Fork it
💻 Explore the code
🚀 Build something amazing!
```
