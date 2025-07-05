import streamlit as st
import pandas as pd
import difflib
import requests
import os
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

movies_data = pd.read_csv('movies.csv')
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')
combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
similarity = cosine_similarity(feature_vectors)

def get_movie_poster(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("Poster") if data.get("Poster") and data.get("Poster") != "N/A" else "https://via.placeholder.com/300x450?text=No+Poster"

def recommend_movies(movie_name):
    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    if not find_close_match:
        return []
    close_match = find_close_match[0]
    index_of_the_movie = movies_data[movies_data.title == close_match].index.values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    recommended_movies = []
    for movie in sorted_similar_movies[1:11]:
        index = movie[0]
        title = movies_data.iloc[index]['title']
        poster = get_movie_poster(title)
        recommended_movies.append((title, poster))
    return recommended_movies

st.title("🎬 Movie Recommender System")

movie_input = st.text_input("Enter your favorite movie")

if st.button("Get Recommendations") and movie_input:
    results = recommend_movies(movie_input)
    if results:
        for title, poster in results:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(poster, use_container_width=True)
            with col2:
                st.subheader(title)
    else:
        st.error("No recommendations found. Try another title.")
