
import sys
import types
import json

from uuid7_fallback import uuid7

# Python-only replacement for uuid_utils
uuid_utils = types.ModuleType("uuid_utils")
uuid_utils.__path__ = []

compat = types.ModuleType("uuid_utils.compat")
compat.uuid7 = uuid7

sys.modules["uuid_utils"] = uuid_utils
sys.modules["uuid_utils.compat"] = compat

import streamlit as st
from generator import generate_interview


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Placement Preparation Assistant",
    page_icon="💼",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM LIGHT THEME
# --------------------------------------------------

st.markdown("""
<style>

/* Main application background */
.stApp {
    background-color: #F8FAFC;
    color: #1E293B;
}

/* Main headings */
h1, h2, h3, h4, h5, h6 {
    color: #172554 !important;
}

/* General text */
.stApp p,
.stApp label,
.stApp li,
.stApp .stMarkdown {
    color: #1E293B;
}

/* Sidebar background */
section[data-testid="stSidebar"] {
    background-color: #F1F5F9 !important;
}

/* Sidebar text */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #1E293B !important;
}

/* Select boxes */
div[data-baseweb="select"] {
    background-color: #FFFFFF !important;
}

div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    border-color: #CBD5E1 !important;
}

div[data-baseweb="select"] input,
div[data-baseweb="select"] span,
div[data-baseweb="select"] div {
    color: #1E293B !important;
}

/* Dropdown menu */
div[data-baseweb="popover"],
ul[role="listbox"],
li[role="option"] {
    background-color: #FFFFFF !important;
    color: #1E293B !important;
}

li[role="option"] * {
    color: #1E293B !important;
}

/* Slider text */
.stSlider label,
.stSlider p,
.stSlider span {
    color: #1E293B !important;
}

/* Input fields */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;
    color: #1E293B !important;
    border: 1px solid #CBD5E1 !important;
}

/* Question cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 12px;
}

/* Expanders */
div[data-testid="stExpander"] {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 8px;
}

div[data-testid="stExpander"] summary {
    background-color: #F1F5F9 !important;
    color: #172554 !important;
}

div[data-testid="stExpander"] summary span {
    color: #172554 !important;
}


/* --------------------------------------------------
   GENERATE INTERVIEW BUTTON
-------------------------------------------------- */

div[data-testid="stFormSubmitButton"] button {
    background-color: #FFFFFF !important;
    color: #4F46E5 !important;
    border: 1px solid #C7D2FE !important;
    border-radius: 8px !important;
    box-shadow: none !important;
    transition: all 0.2s ease-in-out !important;
}

div[data-testid="stFormSubmitButton"] button p {
    color: #4F46E5 !important;
}

/* Generate Button Hover */
div[data-testid="stFormSubmitButton"] button:hover {
    background-color: #EEF2FF !important;
    color: #4338CA !important;
    border: 1px solid #818CF8 !important;
}

div[data-testid="stFormSubmitButton"] button:hover p {
    color: #4338CA !important;
}

/* Generate Button Focus */
div[data-testid="stFormSubmitButton"] button:focus,
div[data-testid="stFormSubmitButton"] button:focus-visible {
    outline: none !important;
    box-shadow: 0 0 0 2px #E0E7FF !important;
}


/* --------------------------------------------------
   DOWNLOAD INTERVIEW JSON BUTTON
-------------------------------------------------- */

.stDownloadButton button {
    background-color: #4F46E5 !important;
    color: #FFFFFF !important;
    border: 1px solid #4F46E5 !important;
    border-radius: 8px !important;
    box-shadow: none !important;
    opacity: 1 !important;
    transition: all 0.2s ease-in-out !important;
}

/* Download Button Text */
.stDownloadButton button p,
.stDownloadButton button span {
    color: #FFFFFF !important;
}

/* Download Button Hover */
.stDownloadButton button:hover {
    background-color: #4338CA !important;
    color: #FFFFFF !important;
    border-color: #4338CA !important;
    opacity: 1 !important;
}

.stDownloadButton button:hover p,
.stDownloadButton button:hover span {
    color: #FFFFFF !important;
}

/* Download Button Focus */
.stDownloadButton button:focus,
.stDownloadButton button:focus-visible,
.stDownloadButton button:active {
    background-color: #4338CA !important;
    color: #FFFFFF !important;
    border-color: #4338CA !important;
    box-shadow: 0 0 0 2px #E0E7FF !important;
}


/* --------------------------------------------------
   METRICS
-------------------------------------------------- */

[data-testid="stMetricValue"] {
    color: #172554 !important;
}

[data-testid="stMetricLabel"] {
    color: #475569 !important;
}

/* Captions */
[data-testid="stCaptionContainer"] {
    color: #64748B !important;
}

/* Main title */
.main-title {
    color: #172554 !important;
    font-size: 34px;
    font-weight: 700;
}

/* Subtitle */
.sub-title {
    color: #475569 !important;
    font-size: 15px;
    margin-bottom: 25px;
}

/* Section heading */
.section-title {
    color: #172554 !important;
    font-size: 21px;
    font-weight: 650;
    margin-top: 20px;
}

/* Question number */
.question-number {
    color: #4F46E5 !important;
    font-size: 14px;
    font-weight: 650;
}

/* Top Streamlit toolbar */
header[data-testid="stHeader"] {
    background-color: #F8FAFC !important;
}

[data-testid="stToolbar"] {
    background-color: #F8FAFC !important;
}

[data-testid="stToolbar"] button,
[data-testid="stStatusWidget"] button {
    color: #1E293B !important;
}

/* Top-right menu and status text */
[data-testid="stStatusWidget"],
[data-testid="stStatusWidget"] * {
    color: #1E293B !important;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">'
    'AI Placement Preparation Assistant'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    'Prepare smarter for your next interview with AI-generated '
    'role-specific questions and answers.'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIDEBAR INPUT FORM
# --------------------------------------------------

with st.sidebar:

    st.title("Interview Setup")

    st.caption("Customize your interview preparation.")

    with st.form("interview_form"):

        job_role = st.selectbox(
            "Job Role",
            [
                "Python Developer",
                "Java Developer",
                "AI Engineer",
                "Machine Learning Engineer",
                "Data Analyst",
                "Data Scientist",
                "GenAI Engineer",
                "Backend Developer",
                "Frontend Developer",
                "Full Stack Developer",
                "Web Developer",
                "Software Engineer",
                "Cloud Engineer",
                "DevOps Engineer",
                "Cybersecurity Engineer",
                "Database Administrator"
            ],
            index=None,
            placeholder="Select a job role"
        )

        experience_level = st.selectbox(
            "Experience Level",
            [
                "Fresher",
                "Entry Level",
                "Intermediate",
                "Experienced"
            ]
        )

        difficulty = st.selectbox(
            "Difficulty",
            [
                "Easy",
                "Medium",
                "Hard",
                "Mixed"
            ]
        )

        num_questions = st.slider(
            "Number of Questions",
            min_value=3,
            max_value=15,
            value=5
        )

        generate_button = st.form_submit_button(
            "Generate Interview",
            type="primary",
            use_container_width=True
        )


# --------------------------------------------------
# GENERATE INTERVIEW
# --------------------------------------------------

if generate_button:

    if job_role is None:

        st.warning("Please select a job role to continue.")

    else:

        with st.spinner("Generating your interview questions..."):

            try:

                response = generate_interview(
                    job_role=job_role,
                    experience_level=experience_level,
                    difficulty=difficulty,
                    num_questions=num_questions
                )

                if hasattr(response, "model_dump"):
                    response_data = response.model_dump()

                elif hasattr(response, "dict"):
                    response_data = response.dict()

                elif isinstance(response, dict):
                    response_data = response

                else:
                    raise ValueError(
                        "Unexpected response format from generate_interview()."
                    )

                st.session_state["interview_data"] = response_data

            except Exception as e:

                st.error(f"Unable to generate interview: {e}")


# --------------------------------------------------
# DISPLAY GENERATED INTERVIEW
# --------------------------------------------------

if "interview_data" in st.session_state:

    data = st.session_state["interview_data"]

    questions = data.get("questions", [])

    st.success("Interview generated successfully!")

    if not questions:

        st.warning(
            "No questions were returned. "
            "Please check your generator.py response schema."
        )

    else:

        st.markdown(
            '<div class="section-title">'
            'Your Interview Questions'
            '</div>',
            unsafe_allow_html=True
        )

        st.caption(
            f"Role: {data.get('job_role', 'Not specified')} | "
            f"Experience: {data.get('experience_level', 'Not specified')}"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Questions", len(questions))

        with col2:
            st.metric(
                "Experience Level",
                data.get("experience_level", "N/A")
            )

        st.divider()

        for index, question in enumerate(questions, start=1):

            with st.container(border=True):

                st.markdown(
                    f'<div class="question-number">'
                    f'QUESTION {index} · '
                    f'{question.get("question_type", "General")}'
                    f'</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"### {question.get('question', '')}"
                )

                st.caption(
                    f"Difficulty: {question.get('difficulty', 'N/A')}"
                )

                with st.expander("View Model Answer and Explanation"):

                    st.markdown("**Model Answer**")
                    st.write(
                        question.get("model_answer", "Not available")
                    )

                    st.markdown("**Explanation**")
                    st.write(
                        question.get("explanation", "Not available")
                    )

                    st.markdown("**Practical Example**")
                    st.write(
                        question.get("practical_example", "Not available")
                    )

                    st.markdown("**Important Keywords**")

                    keywords = question.get("keywords", [])

                    if keywords:
                        st.write(" · ".join(keywords))
                    else:
                        st.write("Not available")

                    st.markdown("**Follow-up Question**")
                    st.write(
                        question.get("follow_up", "Not available")
                    )

        # --------------------------------------------------
        # JSON DOWNLOAD
        # --------------------------------------------------

        st.divider()

        st.markdown("### Export Your Interview")

        json_data = json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        )

        st.download_button(
            label="Download Interview (JSON)",
            data=json_data,
            file_name="interview_questions.json",
            mime="application/json",
            use_container_width=True
        )


else:

    st.markdown(
        '<div class="section-title">Ready to Prepare?</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Enter your job role and interview preferences in the sidebar "
        "to generate personalized interview questions."
    )
