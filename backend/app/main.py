from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, UploadFile, File, Form
from openai import OpenAI
import PyPDF2
import os

# ---------------------------------------------------------
# 1. Load API Key (IMPORTANT)
# ---------------------------------------------------------
load_dotenv()   # <--- loads .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# ---------------------------------------------------------
# 2. Route to analyze resume
# ---------------------------------------------------------
@app.post("/resume/analyze-resume")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    # ---------------------------------------------------------
    # Step A: Read Resume PDF Text
    # ---------------------------------------------------------
    try:
        pdf_reader = PyPDF2.PdfReader(resume.file)
        resume_text = ""

        for page in pdf_reader.pages:
            resume_text += page.extract_text()
    except Exception as e:
        return {"error": f"Failed to read PDF: {str(e)}"}

    # ---------------------------------------------------------
    # Step B: Create prompt for OpenAI
    # ---------------------------------------------------------
    prompt = f"""
    Evaluate this resume for the job role below.

    RESUME:
    {resume_text}

    JOB DESCRIPTION:
    {job_description}

    Provide:
    1. A score out of 100.
    2. Strengths.
    3. Weaknesses.
    4. Missing skills.
    """

    # ---------------------------------------------------------
    # Step C: Call OpenAI API
    # ---------------------------------------------------------
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a resume evaluation expert."},
                {"role": "user", "content": prompt},
            ]
        )

        ai_output = response.choices[0].message["content"]

        return {"analysis": ai_output}

    except Exception as e:
        return {"error": f"OpenAI API error: {str(e)}"}

