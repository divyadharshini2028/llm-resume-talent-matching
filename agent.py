from resume_parser import extract_text_from_pdf
from llm_resume import extract_candidate_info
from job_analyzer import analyze_job_description
from matching import calculate_match


def run_matching_agent(resume_path, job_description):

    print("\n[Agent] Reading resume...")

    resume_text = extract_text_from_pdf(resume_path)

    print("[Agent] Extracting candidate information...")

    candidate = extract_candidate_info(resume_text)

    print("[Agent] Analyzing job description...")

    job = analyze_job_description(job_description)

    print("[Agent] Calculating match...")

    result = calculate_match(candidate, job)

    print("[Agent] Matching completed!")

    return result


if __name__ == "__main__":

    resume_path = "resumes/test_resume.pdf"

    job_description = """
    We are looking for an AI/ML Engineer.

    Required skills:
    Python, Machine Learning, Deep Learning, TensorFlow, SQL.

    Good to have:
    OpenCV, NLP, Docker.

    Education:
    B.Tech or B.E. in Computer Science or related field.
    """

    result = run_matching_agent(
        resume_path,
        job_description
    )

    print("\n========== FINAL RESULT ==========")

    for key, value in result.items():
        print(f"{key}: {value}")