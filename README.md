# Movie Recommendation System (MCA Mini Project)

A complete runnable content-based movie recommender using **TF-IDF text features** and **cosine similarity**, with metadata cleaning, EDA, qualitative evaluation, a Flask web UI, and JSON endpoints.

## Included features
- Starter movie metadata CSV (so the project runs without downloading a dataset).
- Metadata cleaning: missing fields, whitespace, duplicate/blank titles, separators.
- Combined text from genres, plot overview, keywords, cast, and director.
- TF-IDF vectorization and cosine-similarity ranking.
- Search interface and top-10 recommendations.
- API endpoints for recommendations and title lookup.
- EDA and sample-query evaluation scripts.

> `data/movies.csv` is a compact demonstration dataset, not the full MovieLens/TMDB dataset. Replace it with a larger permitted dataset for a full-scale evaluation.

## Folder structure
```text
Movie_Recommendation_System/
├── app.py
├── recommender.py
├── eda.py
├── evaluate.py
├── requirements.txt
├── README.md
├── data/movies.csv
├── models/
├── templates/index.html
└── static/css/style.css
   static/js/script.js
```

## Run on Windows
Open PowerShell in this folder:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python eda.py
python evaluate.py
python app.py
```

Then visit **http://127.0.0.1:5000**.

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that PowerShell window, then activate again. Or skip activation and run `.\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt` and `.\\.venv\\Scripts\\python.exe app.py`.

## API examples
- `http://127.0.0.1:5000/api/recommend?movie=Toy%20Story&limit=5`
- `http://127.0.0.1:5000/api/movies?q=star`

## Dataset schema
CSV columns: `title`, `genres`, `overview`, `keywords`, `cast`, `director`. If using MovieLens, `title` and `genres` are available in `movies.csv`; overview, cast, and director are not provided by the standard MovieLens movie metadata file and will be empty unless enriched. Map TMDB metadata to these columns and save as `data/movies.csv`.

## Methodology
1. Load metadata using Pandas.
2. Clean missing values, whitespace, duplicates, and inconsistent delimiters.
3. Combine metadata into a single text feature per movie.
4. Use TF-IDF to convert text into numerical vectors.
5. Compute pairwise cosine similarity.
6. Rank the most similar movies for a selected title.
7. Inspect sample queries using `evaluate.py`.

## Evaluation
Run `python evaluate.py`. This is qualitative evaluation: inspect whether suggestions share genres, plot themes, cast, or directors. Similarity is a text similarity score, not a probability or a measure of user satisfaction.

## Limitations
- Content-based only; it does not learn from users' ratings or watch history.
- Recommendations depend on metadata quality and catalog size.
- For very large datasets, replace the full similarity matrix with nearest-neighbor or vector-index search.
- Only use datasets in line with their license and terms.
