
# 🎬 Movie Recommender App

A personalized movie recommendation web app built using Streamlit, cosine similarity, and TF-IDF vectorization. It uses the TMDB API to fetch movie posters and lets you explore similar films based on your favorite movie.

## 🚀 Demo

Live soon at: [https://movies.abhijitzende.com](https://movies.abhijitzende.com)

## 📌 Features

- Recommends 5 similar movies based on a selected title
- Fetches real-time posters via TMDB API
- Built using:
  - Python
  - Streamlit
  - Scikit-learn (cosine similarity)
  - TMDB API

## Dataset:

[https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## 📁 Project Structure

```
movie-recommender/
│
├── app.py                  # Streamlit web app
├── model/
│   ├── movie_list.pkl
│   └── similarity.pkl
├── .env                    # Environment file (TMDB API key)
├── .gitignore
├── requirements.txt
└── README.md
```

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Abhiz2411/cinematch.git
   cd cinematch
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your TMDB API key to a `.env` file**
   ```env
   TMDB_API_KEY=your_api_key_here
   ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

## 🌐 Hosting

You can deploy this on:
- Streamlit Cloud
- Render
- Your own domain/subdomain (e.g. `movies.abhijitzende.com`)

## 🧠 How it Works

1. Movies are vectorized using **TF-IDF** based on tags.
2. **Cosine similarity** is used to find similar movies.
3. TMDB API fetches the movie poster and info.

## 📦 Dependencies

- streamlit
- scikit-learn
- pandas
- numpy
- requests
- python-dotenv

## 📃 License

MIT License

---

Made with ❤️ by [Abhijit Zende](https://abhijitzende.com)
