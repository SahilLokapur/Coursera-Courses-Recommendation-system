import os
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

# Load data
courses_list = pickle.load(open('courses.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Load dataset
df = pd.read_csv("Coursera.csv")

# Function to recommend courses
def recommend(course):
    index = df[df['Course Name'] == course].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_courses = []
    
    for i in distances[1:7]:
        course_name = df.iloc[i[0]]['Course Name']
        course_desc = df.iloc[i[0]]['Course Description']
        course_rating = df.iloc[i[0]]['Course Rating']
        course_url = df.iloc[i[0]]['Course URL']
        recommended_courses.append((course_name, course_desc, course_rating, course_url))
    
    recommended_courses.sort(key=lambda x: x[2], reverse=True)  # Sort by rating in descending order
    return recommended_courses

# Page configuration
st.set_page_config(
    page_title="Coursera Course Recommender",
    page_icon="📚",
    layout="wide"
)

# Custom CSS with dark theme
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #ffffff;
        text-align: center;
        margin-bottom: 0.5rem;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #e0e0e0;
        text-align: center;
        margin-bottom: 2rem;
    }
    .recommendation-card {
        background-color: #2c3e50;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid #3498db;
        color: white;
    }
    .footer {
        text-align: center;
        color: #a0a0a0;
        font-size: 0.8rem;
        margin-top: 3rem;
    }
    .section-title {
        color: white;
        font-weight: bold;
    }
    .selected-course {
        color: #3498db;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# Force dark theme background
st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
    }
    </style>
    """, unsafe_allow_html=True)

# App header
st.markdown("<div class='main-header'>📚 Coursera Course Recommendation System</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Find similar courses from a dataset of over 3,000 courses from Coursera!</div>", unsafe_allow_html=True)

# Create two columns for layout
col1, col2 = st.columns([2, 3])

with col1:
    st.markdown("<h3 class='section-title' style='color: white;'>Select a course you like</h3>", unsafe_allow_html=True)
    # Course selection
    course_list = df['Course Name'].values
    st.markdown("<span style='color: white;'>Type or select a course:</span>", unsafe_allow_html=True)
    selected_course = st.selectbox(
        "",
        course_list,
        index=None,
        placeholder="Search for a course...",
    )
    
    # Button to trigger recommendations
    if selected_course:
        recommend_button = st.button('Get Recommendations', type="primary", use_container_width=True)
    else:
        st.info("Please select a course to get recommendations")
        recommend_button = False

# Display recommendations
with col2:
    if selected_course and recommend_button:
        st.markdown("<h3 class='section-title' style='color: white;'>Recommended Courses Similar to:</h3>", unsafe_allow_html=True)
        st.markdown(f"<h4 class='selected-course' style='color: white;'>{selected_course}</h4>", unsafe_allow_html=True)
        
        recommended_courses = recommend(selected_course)
        
        for i, (course, desc, rating, url) in enumerate(recommended_courses):
            st.markdown(f"""
            <div class="recommendation-card">
                <h4>{i+1}. {course} ⭐ {rating}</h4>
                <p>{desc}</p>
                <p><a href="{url}" target="_blank" style="color:#3498db;">Course Link</a></p>
            </div>
            """, unsafe_allow_html=True)
        
        # Add option to export
        st.download_button(
            label="Export Recommendations",
            data=pd.DataFrame(recommended_courses, columns=["Course Name", "Course Description", "Course Rating", "Course URL"]).to_csv().encode('utf-8'),
            file_name="coursera_recommendations.csv",
            mime="text/csv",
        )

# Footer
st.markdown("<div class='footer'>Copyright reserved by Coursera and Respective Course Owners</div>", unsafe_allow_html=True)