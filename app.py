import streamlit as st
from agent import run_matching_agent


# Page configuration
st.set_page_config(
    page_title="AI Resume Talent Matching",
    page_icon="📄",
    layout="wide"
)

# Title
st.title("📄 AI Resume Talent Matching")
st.write(
    "Upload a resume and enter a job description to find the candidate's "
    "suitability using Generative AI."
)

st.divider()

# Resume upload
st.subheader("1. Upload Resume")

uploaded_file = st.file_uploader(
    "Choose a PDF resume",
    type=["pdf"]
)

# Job description
st.subheader("2. Enter Job Description")

job_description = st.text_area(
    "Paste the job description here",
    height=200,
    placeholder="Example: We are looking for a Python and Machine Learning Engineer..."
)

st.divider()

# Analyze button
if st.button("🔍 Analyze Resume", type="primary"):

    if uploaded_file is None:
        st.warning("Please upload a resume PDF.")

    elif not job_description.strip():
        st.warning("Please enter a job description.")

    else:

        # Save uploaded PDF temporarily
        resume_path = "uploaded_resume.pdf"

        with open(resume_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Analyzing resume... Please wait."):

            try:
                result = run_matching_agent(
                    resume_path,
                    job_description
                )

                st.success("Analysis completed successfully! 🎉")

                st.divider()

                # Display result
                st.subheader("📊 Matching Result")

                # Candidate name
                candidate_name = result.get(
                    "candidate_name",
                    "Unknown"
                )

                st.write(f"### 👤 Candidate: {candidate_name}")

                # Match score
                score = result.get(
                    "match_score",
                    0
                )

                st.metric(
                    "Match Score",
                    f"{score}%"
                )

                # Matched skills
                st.subheader("✅ Matched Skills")

                matched_skills = result.get(
                    "matched_required_skills",
                    []
                )

                if matched_skills:
                    st.write(", ".join(matched_skills))
                else:
                    st.write("No matching skills found.")

                # Missing skills
                st.subheader("❌ Missing Skills")

                missing_skills = result.get(
                    "missing_required_skills",
                    []
                )

                if missing_skills:
                    st.write(", ".join(missing_skills))
                else:
                    st.write("No major missing skills.")

                # Preferred skills
                st.subheader("⭐ Preferred Skills Matched")

                preferred_skills = result.get(
                    "matched_preferred_skills",
                    []
                )

                if preferred_skills:
                    st.write(", ".join(preferred_skills))
                else:
                    st.write("None")

                # Recommendation
                st.subheader("💡 Recommendation")

                if score >= 70:
                    st.success(
                        "Strong candidate — recommended for further evaluation."
                    )
                elif score >= 50:
                    st.warning(
                        "Moderate match — candidate may be considered."
                    )
                else:
                    st.error(
                        "Low match — candidate may not be suitable."
                    )

            except Exception as e:

                st.error(
                    "An error occurred while analyzing the resume."
                )

                st.exception(e)