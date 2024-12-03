import streamlit as st
import requests

# Set the API base URL
API_BASE = "http://web-api:4000"  # Match your Docker setup

# Page configuration
st.set_page_config(
    page_title="Skill Tracking and Trends",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Skill Tracking and Trends")

# Job filter dropdown
job_filter = st.selectbox("Select Job Role", ["Software Developer", "Data Scientist", "Marketing Analyst"])

# Fetch data from API endpoints
def fetch_user_skills(user_id):
    try:
        response = requests.get(f"{API_BASE}/students/user_skills/{user_id}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching user skills: {e}")
        return []

def fetch_company_skills(job_filter):
    try:
        response = requests.get(f"{API_BASE}/skills/company_skills", params={"job_filter": job_filter})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching company skills: {e}")
        return []

# Dynamic data fetching
user_id = 1  # Example logged-in user
user_skills = fetch_user_skills(user_id)
company_skills = fetch_company_skills(job_filter)

# Display user and company skills
st.subheader("Skill Comparison")
comparison_data = []
for user_skill in user_skills:
    matching_skill = next((cs for cs in company_skills if cs['name'] == user_skill['name']), None)
    comparison_data.append({
        "User Skill": user_skill["name"],
        "User Proficiency": user_skill["proficiency"],
        "Company Skill": matching_skill["name"] if matching_skill else "N/A",
        "Company Proficiency": matching_skill["proficiency"] if matching_skill else "N/A"
    })
st.table(comparison_data)

# Add new skill for user
st.subheader("Add a New Skill")
new_skill_name = st.text_input("Skill Name")
new_skill_proficiency = st.slider("Proficiency Level", 1, 10, 5)
if st.button("Add Skill"):
    payload = {
        "user_id": user_id,
        "skill_name": new_skill_name,
        "proficiency": new_skill_proficiency
    }
    try:
        response = requests.post(f"{API_BASE}/students/user_skills", json=payload)
        response.raise_for_status()
        st.success("Skill added successfully!")
    except Exception as e:
        st.error(f"Error adding skill: {e}")