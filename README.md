# Movie Recommender System

A Flask-based Movie Recommendation web app that suggests movies similar to your favorite movie using content-based filtering and displays their posters fetched from the OMDB API.

---

## Features

- Content-based movie recommendations based on genres, keywords, cast, director, and tagline.
- Fetches movie posters dynamically using the OMDB API.
- Responsive and attractive UI built with HTML & CSS.
- User-friendly search for movie recommendations.


## Requirements

- Python 3.7+
- Flask
- pandas
- numpy
- scikit-learn
- requests
---

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
6. Add your OMDB API key in app.py:
   ```bash
   OMDB_API_KEY = "your_api_key_here"
8. Run the app:
   ```bash
   python app.py
10. Open http://127.0.0.1:5000 in your browser.

# License
MIT License
