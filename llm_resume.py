import json

from gemini_router import gemini_router


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

    # Send request through the API-key router
    response = gemini_router.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    response_text = response.text.strip()

    # Remove markdown code block if Gemini returns one
    if response_text.startswith("```"):

        response_text = response_text.replace(
            "```json",
            ""
        )

        response_text = response_text.replace(
            "```",
            ""
        )

        response_text = response_text.strip()

    # Convert Gemini response to JSON
    try:

        return json.loads(response_text)

    except json.JSONDecodeError:

        raise ValueError(
            f"Gemini returned invalid JSON:\n{response_text}"
        )


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    from resume_parser import extract_text_from_pdf

    pdf_path = "resumes/test_resume.pdf"

    resume_text = extract_text_from_pdf(
        pdf_path
    )

    candidate = extract_candidate_info(
        resume_text
    )

    print(
        "\n========== CANDIDATE INFORMATION =========="
    )

    print(
        json.dumps(
            candidate,
            indent=4
        )
    )