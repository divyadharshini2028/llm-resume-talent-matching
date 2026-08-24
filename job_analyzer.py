import os
import json
from dotenv import load_dotenv
#from google import genai
from gemini_router import gemini_router

load_dotenv()

#API_KEY = os.getenv("GEMINI_API_KEY")

#if not API_KEY:
    #raise ValueError("GEMINI_API_KEY not found in .env file")

#client = genai.Client(api_key=API_KEY)


def analyze_job_description(job_text: str) -> dict:

    prompt = f"""
You are a job description analysis system.

Read the following job description and extract the important requirements.

Return ONLY valid JSON.

Use exactly this structure:

{{
    "job_title": "",
    "required_skills": [],
    "preferred_skills": [],
    "education": ""
}}

Rules:
- Extract only information present in the job description.
- Do not invent requirements.
- required_skills should contain mandatory technical skills.
- preferred_skills should contain optional or good-to-have skills.
- education should contain the required educational qualification.
- If information is missing, use an empty string or empty list.

Job Description:

{job_text}
"""

    response = gemini_router.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    response_text = response.text.strip()

    if response_text.startswith("```"):
        response_text = response_text.replace("```json", "")
        response_text = response_text.replace("```", "")
        response_text = response_text.strip()

    try:
        return json.loads(response_text)

    except json.JSONDecodeError:
        raise ValueError(
            f"Gemini returned invalid JSON:\n{response_text}"
        )


if __name__ == "__main__":

    job_text = """
    We are looking for an AI/ML Engineer.

    Required skills:
    Python, Machine Learning, Deep Learning, TensorFlow, SQL.

    Good to have:
    OpenCV, NLP, Docker.

    Education:
    B.Tech or B.E. in Computer Science or related field.
    """

    job = analyze_job_description(job_text)

    print("\n========== JOB INFORMATION ==========")
    print(json.dumps(job, indent=4))