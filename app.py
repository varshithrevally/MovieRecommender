from flask import Flask, request, render_template
import pandas as pd
import difflib
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import urllib.parse

app=Flask(__name__)

OMDB_API_KEY="b3f9a715"

movies_data=pd.read_csv('movies.csv')

selected_features=['genres', 'keywords', 'tagline', 'cast', 'director']
for feature in selected_features:
    movies_data[feature]=movies_data[feature].fillna('')

combined_features=movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + \
                    movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + \
                    movies_data['director']

vectorizer=TfidfVectorizer()
feature_vectors=vectorizer.fit_transform(combined_features)

similarity=cosine_similarity(feature_vectors)

def get_movie_poster(title):
    query=urllib.parse.quote(title)
    url=f"http://www.omdbapi.com/?t={query}&apikey={OMDB_API_KEY}"
    response=requests.get(url)
    data=response.json()
    if data.get("Poster") and data["Poster"]!="N/A":
        return data["Poster"]
    else:
        return "https://via.placeholder.com/300x450?text=No+Poster"

def recommend_movies(movie_name):
    list_of_all_titles=movies_data['title'].tolist()
    close_matches=difflib.get_close_matches(movie_name, list_of_all_titles)
    if not close_matches:
        return []
    closest_match=close_matches[0]
    index=movies_data[movies_data.title == closest_match].index.values[0]
    similarity_scores=list(enumerate(similarity[index]))
    sorted_similar_movies=sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    recommended_movies=[]
    for movie in sorted_similar_movies[1:31]:
        idx=movie[0]
        title=movies_data.iloc[idx]['title']
        poster_url=get_movie_poster(title)
        recommended_movies.append({"title": title, "poster": poster_url})
    return recommended_movies

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations=[]
    if request.method=='POST':
        movie_name=request.form['movie_name']
        recommendations=recommend_movies(movie_name)
    return render_template('index.html', recommendations=recommendations)

if __name__=='__main__':
    app.run(debug=True)
