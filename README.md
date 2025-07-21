## Smart ATS: AI-powered Resume and Job Description Matcher
![Static Badge](https://img.shields.io/badge/Python-3.9+-blue?logo=python&labelColor=lightblue&link=https%3A%2F%2Fwww.python.org%2Fdownloads%2F)
![Static Badge](https://img.shields.io/badge/Streamlit-lightblue?logo=streamlit&link=https%3A%2F%2Fdocs.streamlit.io%2F)
![Static Badge](https://img.shields.io/badge/PyPDF-red)
![Static Badge](https://img.shields.io/badge/Gemini-1.5%20Flash-white?logo=googlegemini&logoColor=%2300B0FF&labelColor=white)
![Static Badge](https://img.shields.io/badge/.ENV-white?logo=dotenv)


**Smart ATS** is an AI-powered tool designed to analyze resumes against job descriptions and provide detailed insights into their compatibility. It generates a resume match percentage, highlights strengths and weaknesses, and provides tailored recommendations for improving the resume to fit a specific job role. This tool uses Google's **Gemini 1.5 Flash** model for natural language processing, enabling quick and accurate evaluations.

### Key Features:

* **Resume Match Percentage:** A numerical score indicating how well a resume aligns with a job description.
* **Strengths & Weaknesses:** Detailed analysis of the candidate's strengths and areas that need improvement based on the job requirements.
* **Recommendations:** AI-generated suggestions for enhancing the resume to better fit the job.
* **Overall Summary:** A concise evaluation of the candidate's suitability for the role.

### How to Run the Project:

1. **Install Dependencies:**

   First, make sure you have all the required libraries by installing them via `requirements.txt`.

   To install dependencies, run:

   ```bash
   pip install -r requirements.txt
   ```

2. **Create a `.env` file for API Key:**

   You’ll need to set up your API key for **Google Gemini** in the `.env` file.

   Go to https://makersuite.google.com/app/apikey/ and create new API key

   ```dotenv
   GOOGLE_API_KEY=your_google_api_key_here
   ```

   Make sure to replace `your_google_api_key_here` with your actual Google API key.

4. **Run the App:**

   To run the app, simply use Streamlit:

   ```bash
   streamlit run app.py
   ```

   Replace `app.py` with the filename of the script containing the code.

### How it Works:

1. **Job Description Input:** Paste the job description into the text area provided.
2. **Resume Upload:** Upload your resume in PDF format.
3. **Click "Analyze Resume":** The app will process the resume and job description, providing detailed feedback including a match percentage, strengths, weaknesses, and recommendations.
4. **Review the Results:** The analysis will appear on the screen.

### Requirements:

* **Python 3.9+**
* **Libraries:**

  * **Streamlit**: For building the web application interface.
  * **Google Generative AI**: For analyzing the job description and resume with Gemini model.
  * **PyPDF**: For extracting text from PDF resumes.
  * **Python-dotenv**: To manage API keys and environment variables.

### Notes:

* Make sure the `.env` file is located in the same directory as the script.

