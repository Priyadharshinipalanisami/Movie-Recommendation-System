# 🎬 Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Content--Based-orange)
![Framework](https://img.shields.io/badge/Framework-Flask-green)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A Machine Learning-based Movie Recommendation System that recommends similar movies using **TF-IDF Vectorization and Cosine Similarity**. The project includes movie metadata preprocessing, Exploratory Data Analysis (EDA), recommendation evaluation, and an interactive Flask web application.

## 📌 Project Overview

The Movie Recommendation System helps users discover movies similar to a selected title. It analyzes movie metadata, including genres, keywords, and descriptions, to calculate similarity scores and rank relevant movies.

This project demonstrates the practical application of machine learning, text processing, and web development in building a recommendation system.

## ✨ Features

- 🎥 Content-based movie recommendations
- 🧹 Movie metadata preprocessing and cleaning
- 🔍 TF-IDF text feature extraction
- 📊 Cosine Similarity-based ranking
- 📈 Exploratory Data Analysis (EDA)
- 🌐 Interactive Flask web application
- 🔗 REST API for movie recommendations
- 🧪 Qualitative evaluation using sample movie queries
- 📱 Simple and user-friendly interface

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data processing and cleaning |
| NumPy | Numerical operations |
| Scikit-learn | TF-IDF and similarity calculations |
| Flask | Web application and API |
| HTML5 | Web page structure |
| CSS3 | User interface styling |
| JavaScript | Frontend interactions |
| CSV | Sample movie dataset storage |

## 🧠 Recommendation Methodology

1. **Data Collection:** Load movie metadata from the provided CSV dataset.
2. **Data Preprocessing:** Clean and prepare relevant movie fields.
3. **Feature Engineering:** Combine available text metadata such as genres, keywords, and descriptions.
4. **TF-IDF Vectorization:** Convert text features into numerical vectors.
5. **Cosine Similarity:** Calculate similarity between movie vectors.
6. **Recommendation Ranking:** Rank movies by similarity and return the top matches.
7. **Evaluation:** Test the recommender using sample movie titles.
8. **Web Integration:** Display recommendations through the Flask application.

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── recommender.py
├── eda.py
├── evaluate.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── data/
│   └── movies.csv
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or a compatible version
- pip package manager
- Git
- A web browser

### Step 1: Clone the Repository

```bash
git clone Movie_Recmmendation_System_URL
cd Movie-Recommendation-System
```

Replace `Movie_Recommendation_System_URL` with your actual GitHub repository URL.

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 3: Activate the Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run Exploratory Data Analysis

```bash
python eda.py
```

This script analyzes the available movie dataset and provides basic dataset insights.

### Step 6: Evaluate Recommendations

```bash
python evaluate.py
```

This script tests recommendations for sample movie titles and displays ranked results with similarity scores.

### Step 7: Start the Flask Application

```bash
python app.py
```

Open the following URL in your browser:

```text
http://127.0.0.1:5000
```

## 🔗 API Usage

The application provides API endpoints for movie search and recommendations.

### Get Movie Recommendations

Example:

```text
/api/recommend?movie=Toy%20Story&limit=5
```

This endpoint returns recommendations for the selected movie, subject to the movies available in the dataset.

### Search for Movies

Example:

```text
/api/movies?q=star
```

This endpoint searches the available movie titles using the supplied query.

**Note:** The API endpoints are accessed through the running Flask application at `http://127.0.0.1:5000`.

## 📊 Sample Evaluation

The recommender can be tested using movie titles such as:

- Toy Story
- The Matrix
- Finding Nemo
- The Dark Knight
- Titanic
- Dune

For example, a query for **Toy Story** may recommend *Toy Story 2*, *Up*, and *Finding Nemo* because of similarities in their available metadata.

Similarity scores indicate relative similarity between movie feature vectors. They are not probabilities, ratings, or guarantees that a user will enjoy a movie.

## 📈 Expected Results

- A ranked list of movies similar to the selected title
- Similarity scores for recommended movies
- Basic insights from Exploratory Data Analysis
- Successful API responses for supported queries
- An interactive web interface for exploring recommendations

Actual results depend on the contents and quality of the dataset.

## 🚀 Future Enhancements

- Integrate larger MovieLens or TMDB datasets
- Add collaborative filtering using user ratings
- Develop a hybrid recommendation approach
- Add movie posters and detailed movie information
- Introduce user accounts and personalized watchlists
- Evaluate ranking quality using Precision@K, Recall@K, or NDCG
- Deploy the application to a cloud hosting platform

## 🎯 Learning Outcomes

This project demonstrates practical experience in:

- Machine learning recommendation techniques
- Text preprocessing and feature extraction
- TF-IDF Vectorization and Cosine Similarity
- Data cleaning and exploratory analysis
- Python web application development with Flask
- REST API implementation and qualitative evaluation

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👩‍💻 Author

**Priyadharshini**

GitHub:(https://github.com/Priyadharshinipalanisami)

LinkedIn: (https://www.linkedin.com/in/priyadharshini-pazhanisamy-224229360/)

---

⭐ If you find this project useful, consider giving the repository a star!
