from pathlib import Path
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, csv_path="data/movies.csv"):
        path = Path(csv_path)
        if not path.exists():
            raise FileNotFoundError(f"{path} not found. Ensure data/movies.csv exists.")
        self.movies = self.clean_metadata(pd.read_csv(path))
        if self.movies.empty:
            raise ValueError("No valid movie rows found in the dataset.")
        self.movies["features"] = self.movies.apply(self._features, axis=1)
        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        self.matrix = self.vectorizer.fit_transform(self.movies["features"])
        self.similarity = cosine_similarity(self.matrix, self.matrix)

    @staticmethod
    def clean_metadata(df):
        df = df.copy()
        for col in ["title", "genres", "overview", "keywords", "cast", "director"]:
            if col not in df.columns:
                df[col] = ""
            df[col] = df[col].fillna("").astype(str).str.strip()
        df["title"] = df["title"].str.replace(r"\s+", " ", regex=True)
        df = df[df["title"].ne("")].drop_duplicates(subset=["title"]).reset_index(drop=True)
        for col in ["genres", "keywords", "cast", "director"]:
            df[col] = df[col].str.replace("|", " ", regex=False).str.replace(",", " ", regex=False)
        df["overview"] = df["overview"].str.replace(r"\s+", " ", regex=True)
        return df

    @staticmethod
    def _features(row):
        # Repeating genres gives genre overlap extra weight.
        return " ".join([row["genres"], row["genres"], row["keywords"],
                         row["overview"], row["cast"], row["director"]]).lower()

    @staticmethod
    def _normalize(value):
        return re.sub(r"[^a-z0-9]+", "", str(value).lower())

    def recommend(self, query, top_n=10):
        query = str(query).strip()
        if not query:
            return []
        normalized = self._normalize(query)
        titles = self.movies["title"].astype(str)
        exact = [i for i, t in enumerate(titles) if self._normalize(t) == normalized]
        if exact:
            idx = exact[0]
        else:
            partial = [i for i, t in enumerate(titles) if normalized in self._normalize(t)]
            if partial:
                idx = min(partial, key=lambda i: len(titles.iloc[i]))
            else:
                from difflib import SequenceMatcher
                scores = [SequenceMatcher(None, normalized, self._normalize(t)).ratio() for t in titles]
                idx = max(range(len(scores)), key=scores.__getitem__)
                if scores[idx] < 0.45:
                    return []
        ranked = self.similarity[idx].argsort()[::-1]
        results = []
        for j in ranked:
            if j == idx:
                continue
            row = self.movies.iloc[int(j)]
            results.append({"title": row["title"], "genres": row["genres"],
                            "overview": row["overview"],
                            "similarity": round(float(self.similarity[idx, j]), 3)})
            if len(results) >= max(1, int(top_n)):
                break
        return results

if __name__ == "__main__":
    rec = MovieRecommender()
    print(f"Loaded {len(rec.movies)} movies")
    for item in rec.recommend("Toy Story", 5):
        print(item)
