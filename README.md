# 🎬 Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on genres, keywords, tagline, cast, and director using Natural Language Processing (NLP) and cosine similarity. Built using Python, Streamlit, and the OMDB API.

🔗 **Live App**: https://movierecommendationsyst.streamlit.app/

---

## 📌 Features

- 🎥 Recommend 10 movies similar to your favorite
- 📊 Uses TF-IDF and cosine similarity for smart recommendations
- 🧠 Fetches movie posters from the OMDB API
- 🧱 Streamlit web interface — clean, fast, and responsive
- ☁️ Deployed on **Streamlit Cloud**

---

## 🛠 Tech Stack

- **Python**
- **Pandas & scikit-learn** (TF-IDF, cosine similarity)
- **Streamlit** (UI & hosting)
- **OMDB API** (poster fetching)
- **dotenv / st.secrets** (API key handling)

---

## 🚀 Getting Started (Run Locally)

1. Clone this repository
git clone https://github.com/varshithrevally/MovieRecommender.git

2. Go to Directory in cmd
cd MovieRecommender

3. Install dependencies
pip install -r requirements.txt

4. Create a .env file (for local run)
OMDB_API_KEY=your_omdb_api_key_here

4.streamlit run app.py


💡 Future Enhancements
🎞 Add trailer previews via YouTube API

⭐ Include IMDb ratings and runtime

📊 Add genre filters and sorting

🙌 Acknowledgements
OMDB API

Streamlit

scikit-learn



