# Coursera-Courses-Recommendation-system
Overview
The Coursera Course Recommendation System is a machine learning-based web application that helps users find similar courses based on their interests. The system is built using Streamlit, Python, and precomputed similarity models to provide quick and accurate recommendations.

With a dataset of over 3,000 Coursera courses, this application suggests courses similar to the one selected by the user, ranking them based on their relevance and rating.

Features
Find Similar Courses – Get personalized recommendations based on course content and similarity scores.
Precomputed Similarity Matrix – Uses cosine similarity and text-based similarity for fast recommendations.
User-Friendly Interface – Built with Streamlit, featuring an intuitive design and dark-themed UI.
Course Details & Ratings – Displays course descriptions, ratings, and direct links to Coursera.
Export Recommendations – Save the recommended courses as a CSV file for later reference.

How It Works
Select a course from the dropdown menu.
The system retrieves similar courses using a precomputed similarity matrix.
Recommendations are ranked based on similarity and course ratings.
Users can view course details and export recommendations as a CSV file.
Technology Stack
Frontend: Streamlit (for UI)
Backend: Python (for recommendation logic)
Data Processing: Pandas, NumPy
Machine Learning: Scikit-learn (for similarity computation)
Storage: Pickle (.pkl) files for fast data retrieval
