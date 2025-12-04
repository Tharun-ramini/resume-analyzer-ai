from fastapi import APIRouter, UploadFile, File, Form
from openai import OpenAI
import os
from backend.app.resume_parser import extract_text_from_pdf

router = APIRouter()

# Load API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@router.post("/analyze-resume")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    # --------------------------
    # 1. Save uploaded file
    # --------------------------
    temp_path = "temp_resume.pdf"
    resume_bytes = await resume.read()

    with open(temp_path, "wb") as f:
        f.write(resume_bytes)

    # --------------------------
    # 2. Extract text
    # --------------------------
    resume_text = extract_text_from_pdf(temp_path)

    # --------------------------
    # 3. Create prompt
    # --------------------------
    prompt = f"""
    You are an AI resume evaluator.

    Compare the resume and job description below.
    Provide:

    1. Match score (0–100)
    2. Strengths
    3. Weaknesses
    4. Short explanation

    --- JOB DESCRIPTION ---
    {job_description}

    --- RESUME TEXT ---
    {resume_text}
    """

    # --------------------------
    # 4. Query OpenAI API
    # --------------------------
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.choices[0].message["content"]

        return {
            "status": "success",
            "analysis": output
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

