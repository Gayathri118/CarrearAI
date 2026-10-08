# CareerAI – Smart Career Guidance & Job Matching

## Project idea
CareerAI is an AI-inspired career guidance web application based on the SDG 8 project direction in the supplied IBM SkillsBuild Lean Canvas material: resume/career guidance and job prediction based on skills and location.

## Features
- Skill and interest input
- Preferred location input
- Career-role matching
- Match percentage
- Matched skills display
- Skill-gap / next-learning suggestions
- Simple responsive UI
- Flask REST API backend

## Tech stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- Data: Local Python dataset
- Matching: weighted skill/location/interest scoring

## Run
1. Install Python 3.10+
2. Open terminal inside this folder.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Start:
   `python backend/app.py`
5. Open:
   `http://127.0.0.1:5000`

## Example
Skills: Python, SQL
Interests: Data
Location: Chennai

The app will rank Data Analyst and Python Developer among the suitable paths and show missing skills.

## Future enhancements
- Upload and parse resumes
- Real job API integration
- ML-based recommendation model
- User login and profile history
- Course recommendations
- Tamil/regional language support
