from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app=Flask(__name__)


movies_data=pd.read_csv('movies.csv')

selected_features=['genres', 'keywords', 'tagline', 'cast', 'director']
for feature in selected_features:
    movies_data[feature]=movies_data[feature].fillna('')

combined_features=movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']

vectorizer=TfidfVectorizer()
feature_vectors=vectorizer.fit_transform(combined_features)

similarity=cosine_similarity(feature_vectors)

def recommend_movies(movie_name):
    list_of_all_titles=movies_data['title'].tolist()
    find_close_match=difflib.get_close_matches(movie_name, list_of_all_titles)
    if not find_close_match:
        return ["No similar movies found."]
    close_match=find_close_match[0]
    index_of_the_movie=movies_data[movies_data.title == close_match].index.values[0]
    similarity_score=list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies=sorted(similarity_score, key=lambda x: x[1], reverse=True)
    recommended_movies=[]
    for movie in sorted_similar_movies[1:31]:
        index=movie[0]
        title=movies_data.iloc[index]['title']
        recommended_movies.append(title)
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
