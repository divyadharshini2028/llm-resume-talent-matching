import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=API_KEY)


def extract_candidate_info(resume_text: str) -> dict:
    prompt = f"""
You are a resume information extraction system.

Read the resume text below and extract the candidate information.

Return ONLY valid JSON.
Do not use markdown.
Do not add explanations.

Use exactly this structure:

{{
    "name": "",
    "email": "",
    "education": "",
    "skills": [],
    "projects": [],
    "certifications": []
}}

Rules:
- Extract information only from the resume.
- Do not invent information.
- skills must be a list.
- projects must be a list of project names.
- certifications must be a list of certification names.
- If something is missing, use an empty string or empty list.

Resume text:

{resume_text}
"""

    response = client.models.generate_content(model="gemini-3.6-flash", contents=prompt)

    response_text = response.text.strip()

    if response_text.startswith("```"):
        response_text = response_text.replace("```json", "")
        response_text = response_text.replace("```", "")
        response_text = response_text.strip()

    try:
        return json.loads(response_text)

    except json.JSONDecodeError:
        raise ValueError(f"Gemini returned invalid JSON:\n{response_text}")


if __name__ == "__main__":
    from resume_parser import extract_text_from_pdf

    pdf_path = "resumes/test_resume.pdf"

    resume_text = extract_text_from_pdf(pdf_path)

    candidate = extract_candidate_info(resume_text)

    print("\n========== CANDIDATE INFORMATION ==========")
    print(json.dumps(candidate, indent=4))
