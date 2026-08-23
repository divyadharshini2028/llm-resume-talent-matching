import streamlit as st
from agent import run_matching_agent


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="TalentMatch AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# HELPER FOR HTML
# ============================================================

def html(content):
    st.markdown(content, unsafe_allow_html=True)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background: radial-gradient(circle at top left, #eef2ff 0%, #f8f9ff 35%, #ffffff 75%);
}

.main {
    padding-top: 1rem;
}

#MainMenu, footer {
    visibility: hidden;
}

/* HERO */
.hero-wrapper {
    background: linear-gradient(135deg, #4f46e5, #7c3aed, #c026d3);
    padding: 4px;
    border-radius: 28px;
    margin-top: 10px;
    margin-bottom: 35px;
    box-shadow: 0 20px 50px rgba(79, 70, 229, 0.25);
}

.hero {
    background: rgba(255, 255, 255, 0.96);
    border-radius: 24px;
    padding: 40px 20px;
    text-align: center;
}

.hero-icon {
    font-size: 55px;
    margin-bottom: 10px;
}

.hero-title {
    font-size: 42px;
    font-weight: 900;
    background: linear-gradient(90deg, #4338ca, #7c3aed, #c026d3);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 8px;
}

.hero-subtitle {
    font-size: 20px;
    font-weight: 700;
    color: #374151;
    margin-bottom: 10px;
}

.hero-description {
    font-size: 15px;
    color: #6b7280;
}

/* SECTION TITLE */
.section-title {
    font-size: 26px;
    font-weight: 900;
    color: #1f2937;
    margin-top: 15px;
    margin-bottom: 20px;
}

/* INPUT CARDS */
.input-card {
    padding: 20px;
    border-radius: 20px;
    min-height: 120px;
    margin-bottom: 15px;
    background: rgba(255,255,255,0.95);
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
}

.resume-card {
    border: 2px solid #93c5fd;
    background: linear-gradient(135deg, #eff6ff, #ffffff);
}

.job-card {
    border: 2px solid #f9a8d4;
    background: linear-gradient(135deg, #fdf2f8, #ffffff);
}

.card-title {
    font-size: 20px;
    font-weight: 800;
    color: #1f2937;
    margin-bottom: 8px;
}

.card-description {
    font-size: 14px;
    color: #6b7280;
    line-height: 1.5;
}

/* FILE UPLOADER & TEXTAREA */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.95);
    border-radius: 16px;
    padding: 10px;
    border: 1px solid #dbeafe;
}

textarea {
    border-radius: 15px !important;
    border: 2px solid #e5e7eb !important;
    background: #ffffff !important;
    font-size: 15px !important;
}

textarea:focus {
    border: 2px solid #8b5cf6 !important;
    box-shadow: 0 0 0 3px rgba(139,92,246,0.12) !important;
}

/* ANALYZE BUTTON */
div.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 16px;
    border: none;
    background: linear-gradient(90deg, #4f46e5, #7c3aed, #c026d3);
    color: white;
    font-size: 18px;
    font-weight: 800;
    box-shadow: 0 12px 30px rgba(124,58,237,0.3);
    transition: all 0.25s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 18px 40px rgba(124,58,237,0.4);
}

/* RESULT CARDS & SKILL BADGES */
.result-box {
    background: white;
    border-radius: 18px;
    padding: 20px;
    margin-top: 15px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
}

.skill {
    display: inline-block;
    padding: 8px 14px;
    margin: 4px;
    border-radius: 30px;
    font-size: 14px;
    font-weight: 600;
}

.matched-skill { background: #dcfce7; color: #166534; border: 1px solid #86efac; }
.missing-skill { background: #fee2e2; color: #991b1b; border: 1px solid #fca5a5; }
.preferred-skill { background: #fef3c7; color: #92400e; border: 1px solid #fcd34d; }

/* SCORE */
.score-card {
    text-align: center;
    background: linear-gradient(135deg, #eef2ff, #faf5ff);
    border-radius: 20px;
    padding: 20px;
    border: 1px solid #c4b5fd;
    box-shadow: 0 10px 30px rgba(99,102,241,0.12);
}

.score-number {
    font-size: 50px;
    font-weight: 900;
    background: linear-gradient(90deg, #4f46e5, #c026d3);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.score-label {
    font-size: 14px;
    color: #6b7280;
    font-weight: 600;
}

/* FOOTER */
.footer {
    margin-top: 50px;
    padding: 20px;
    text-align: center;
    background: white;
    border-radius: 16px;
    color: #6b7280;
    border: 1px solid #e5e7eb;
    box-shadow: 0 5px 20px rgba(0,0,0,0.04);
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO SECTION
# ============================================================

html("""
<div class="hero-wrapper">
    <div class="hero">
        <div class="hero-icon">🤖</div>
        <div class="hero-title">TalentMatch AI</div>
        <div class="hero-subtitle">Intelligent Resume Screening & Talent Matching</div>
        <div class="hero-description">Powered by Generative AI and intelligent matching agents</div>
    </div>
</div>
""")


# ============================================================
# CANDIDATE ANALYSIS
# ============================================================

html('<div class="section-title">📋 Candidate Analysis</div>')


# ============================================================
# TWO INPUT COLUMNS
# ============================================================

left_col, right_col = st.columns(2, gap="large")


# ============================================================
# RESUME
# ============================================================

with left_col:
    html("""
    <div class="input-card resume-card">
        <div class="card-title">📄 Resume</div>
        <div class="card-description">Upload the candidate's PDF resume for AI-powered analysis.</div>
    </div>
    """)

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"],
        label_visibility="collapsed"
    )


# ============================================================
# JOB DESCRIPTION
# ============================================================

with right_col:
    html("""
    <div class="input-card job-card">
        <div class="card-title">💼 Job Description</div>
        <div class="card-description">Enter the requirements and skills for the position.</div>
    </div>
    """)

    job_description = st.text_area(
        "Job Description",
        placeholder=(
            "Example:\n\n"
            "We are looking for an AI/ML Engineer.\n\n"
            "Required skills: Python, Machine Learning, "
            "Deep Learning, TensorFlow, SQL.\n\n"
            "Preferred skills: OpenCV, NLP, Docker."
        ),
        height=220,
        label_visibility="collapsed"
    )


# ============================================================
# ANALYZE BUTTON
# ============================================================

st.write("")

button_col = st.columns([1, 2, 1])[1]

with button_col:
    analyze_button = st.button(
        "🚀  Analyze Candidate",
        type="primary",
        use_container_width=True
    )


# ============================================================
# ANALYSIS
# ============================================================

if analyze_button:

    if uploaded_file is None:
        st.warning("📄 Please upload a resume PDF before analyzing.")
        st.stop()

    if not job_description.strip():
        st.warning("💼 Please enter a job description before analyzing.")
        st.stop()

    resume_path = "uploaded_resume.pdf"

    with open(resume_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    with st.spinner("🤖 AI agents are analyzing the candidate..."):
        try:
            result = run_matching_agent(
                resume_path,
                job_description
            )

            st.success("✅ Candidate analysis completed successfully!")
            st.divider()

            html('<div class="section-title">📊 Matching Results</div>')

            candidate_name = result.get("candidate_name", "Unknown Candidate")
            job_title = result.get("job_title", "Job Position")
            score = result.get("match_score", 0)

            try:
                score = float(score)
            except:
                score = 0.0

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("👤 Candidate", candidate_name)

            with col2:
                st.metric("💼 Position", job_title)

            with col3:
                st.metric("🎯 Match Score", f"{score:.1f}%")

            st.write("")

            html(f"""
            <div class="score-card">
                <div class="score-number">{score:.1f}%</div>
                <div class="score-label">Candidate Compatibility Score</div>
            </div>
            """)

            st.progress(min(max(score / 100, 0.0), 1.0))

            st.write("")

            if score >= 70:
                st.success("🌟 Strong Candidate — Recommended for further evaluation.")
            elif score >= 50:
                st.warning("👍 Moderate Candidate — Consider for further evaluation.")
            else:
                st.error("⚠️ Low Match — Candidate may not be suitable for this role.")

            st.write("")

            matched_col, missing_col = st.columns(2)

            with matched_col:
                html('<div class="result-box"><h3>✅ Matched Skills</h3></div>')
                matched_skills = result.get("matched_required_skills", [])
                if matched_skills:
                    skill_html = "".join([f'<span class="skill matched-skill">✓ {s}</span>' for s in matched_skills])
                    st.markdown(skill_html, unsafe_allow_html=True)
                else:
                    st.info("No required skills matched.")

            with missing_col:
                html('<div class="result-box"><h3>❌ Missing Skills</h3></div>')
                missing_skills = result.get("missing_required_skills", [])
                if missing_skills:
                    skill_html = "".join([f'<span class="skill missing-skill">• {s}</span>' for s in missing_skills])
                    st.markdown(skill_html, unsafe_allow_html=True)
                else:
                    st.success("🎉 No major skill gaps identified.")

            st.write("")

            html('<div class="result-box"><h3>⭐ Preferred Skills Matched</h3></div>')
            preferred_skills = result.get("matched_preferred_skills", [])
            if preferred_skills:
                skill_html = "".join([f'<span class="skill preferred-skill">★ {s}</span>' for s in preferred_skills])
                st.markdown(skill_html, unsafe_allow_html=True)
            else:
                st.info("No preferred skills matched.")

            st.write("")
            st.divider()

            html('<div class="section-title">💡 Recruitment Recommendation</div>')

            if score >= 70:
                st.markdown(f"### 🌟 Strong Match\n\n**{candidate_name}** shows strong alignment with the **{job_title}** role.")
            elif score >= 50:
                st.markdown(f"### 👍 Moderate Match\n\n**{candidate_name}** shows moderate alignment with the **{job_title}** role.")
            else:
                st.markdown(f"### ⚠️ Low Match\n\n**{candidate_name}** currently shows limited alignment with the **{job_title}** role.")

            st.write("")
            with st.expander("🔎 View detailed AI matching data"):
                st.json(result)

        except Exception as error:
            st.error("❌ Something went wrong during analysis.")
            with st.expander("View technical error"):
                st.exception(error)


# ============================================================
# FOOTER
# ============================================================

html("""
<div class="footer">
    🤖 <strong>TalentMatch AI</strong> &nbsp;|&nbsp; Generative AI & Intelligent Agents &nbsp;|&nbsp; Campus Placement Assistant
</div>
""")