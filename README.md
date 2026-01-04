Features

Upload resumes in PDF / DOCX format

Enter job description for targeted analysis

Extracts resume text automatically

AI-generated analysis including:

Resume score (ATS-style)

Missing skills

Improvement suggestions

Optimized resume summary

Clean & responsive frontend UI

Secure API key management using .env

Modular backend architecture

Tech Stack
Backend

Python

FastAPI

OpenAI API

PyPDF2

python-docx

python-multipart

Uvicorn

Frontend

HTML

Tailwind CSS

JavaScript

Tools

Git & GitHub

VS Code

Setup Instructions
1.Clone the Repository
git clone https://github.com/yourusername/resume-analyzer-ai.git
cd resume-analyzer-ai
2.Backend Setup
python -m venv .venv
--Activate Virtual Environment
Windows
.venv\Scripts\activate
pip install -r requirements.txt
3.Create a .env file inside the backend folder:
OPENAI_API_KEY=your_openai_api_key_here
4.Run server
uvicorn backend.app.main:app --reload
http://127.0.0.1:8000
5.Create Frontend


API Endpoint
Analyze Resume
POST /resume/analyze-resume
Form Data:
--file → Resume file (PDF/DOCX)
--job_description → Job description text



