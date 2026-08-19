def normalize_skill(skill):
    return skill.strip().lower()


def calculate_match(candidate, job):
    candidate_skills = {
        normalize_skill(skill)
        for skill in candidate.get("skills", [])
    }

    required_skills = {
        normalize_skill(skill)
        for skill in job.get("required_skills", [])
    }

    preferred_skills = {
        normalize_skill(skill)
        for skill in job.get("preferred_skills", [])
    }

    matched_required = candidate_skills.intersection(required_skills)
    missing_required = required_skills - candidate_skills

    matched_preferred = candidate_skills.intersection(preferred_skills)

    if required_skills:
        required_score = (
            len(matched_required) / len(required_skills)
        ) * 100
    else:
        required_score = 0

    if preferred_skills:
        preferred_score = (
            len(matched_preferred) / len(preferred_skills)
        ) * 100
    else:
        preferred_score = 0

    final_score = (
        required_score * 0.8
        + preferred_score * 0.2
    )

    return {
        "candidate_name": candidate.get("name", ""),
        "job_title": job.get("job_title", ""),
        "match_score": round(final_score, 2),
        "matched_required_skills": sorted(matched_required),
        "missing_required_skills": sorted(missing_required),
        "matched_preferred_skills": sorted(matched_preferred)
    }


if __name__ == "__main__":

    candidate = {
        "name": "ANANYA RAJARAMAN",
        "skills": [
            "Python",
            "SQL",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "OpenCV"
        ]
    }

    job = {
        "job_title": "AI/ML Engineer",
        "required_skills": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "SQL"
        ],
        "preferred_skills": [
            "OpenCV",
            "NLP",
            "Docker"
        ]
    }

    result = calculate_match(candidate, job)

    print("\n========== MATCH RESULT ==========")
    print(result)