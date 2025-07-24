import streamlit as st
import os
import google.generativeai as genai
from pypdf import PdfReader

# using API key from environment variables of streamlit cloud
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("Google API key is missing. Please set it in your environment.")
    st.stop()

# If you use dotenv for local development with .env file
# from dotenv import load_dotenv
# load_dotenv()


genai.configure(api_key=GOOGLE_API_KEY)

device = "gpu" if os.getenv("USE_GPU", "false").lower() == "true" else "cpu"

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_file):
    text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def get_gemini_response(job_description, resume_text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"""
    Act as a highly experienced Human Resource Manager.
    Your task is to analyze the provided resume against the given job description.
    Please provide the following:

    1.  **Resume Match Percentage:** A numerical percentage indicating how well the resume matches the job description.
    2.  **Strengths:** List the key strengths of the candidate based on the resume's alignment with the job description.
    3.  **Weaknesses/Missing Skills:** Identify any missing skills or areas where the resume doesn't align with the job requirements.
    4.  **Recommendations:** Provide specific recommendations to improve the resume for this particular job.
    5.  **Overall Summary:** A brief summary of the candidate's suitability for the job based on the resume.

    **Job Description:**
    {job_description}

    **Resume:**
    {resume_text}
    """
    response = model.generate_content(prompt)
    return response.text

#  5.  **Cover Letter:** Generate a cover letter tailored to the job description based on the resume.

# Streamlit App
st.set_page_config(page_title="ATS Resume Tracker", layout="wide")
st.title("Smart ATS")
# st.header("ATS Resume Tracker")
st.subheader("Match your resume to job descriptions with AI!")

job_description = st.text_area("Paste the Job Description here:")
uploaded_resume = st.file_uploader("Upload your resume (PDF only):", type=["pdf"])

if st.button("Analyze Resume"):
    if job_description and uploaded_resume:
        resume_text = get_pdf_text(uploaded_resume)
        gemini_analysis = get_gemini_response(job_description, resume_text)

        st.subheader("Resume Analysis:")
        st.markdown(gemini_analysis)

    elif not job_description:
        st.warning("Please paste the Job Description.")
    elif not uploaded_resume:
        st.warning("Please upload a resume (PDF).")
