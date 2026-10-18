from flask import Flask, render_template, request, jsonify
from recommender import MovieRecommender

app = Flask(__name__)
engine = MovieRecommender("data/movies.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    query, recommendations, error = "", [], None
    if request.method == "POST":
        query = request.form.get("movie", "").strip()
        if query:
            recommendations = engine.recommend(query, 10)
            if not recommendations:
                error = f'No close match found for "{query}". Try another title.'
        else:
            error = "Please enter a movie title."
    return render_template("index.html", query=query, recommendations=recommendations,
                           error=error, movie_count=len(engine.movies))

@app.route("/api/recommend")
def api_recommend():
    query = request.args.get("movie", "").strip()
    try:
        limit = max(1, min(int(request.args.get("limit", 10)), 25))
    except ValueError:
        limit = 10
    if not query:
        return jsonify({"error": "Use ?movie=Toy%20Story"}), 400
    return jsonify({"query": query, "recommendations": engine.recommend(query, limit)})

@app.route("/api/movies")
def api_movies():
    q = request.args.get("q", "").lower().strip()
    titles = engine.movies["title"].astype(str)
    matches = titles[titles.str.lower().str.contains(q, regex=False)].head(20).tolist() if q else titles.head(20).tolist()
    return jsonify({"movies": matches})

if __name__ == "__main__":
    app.run(debug=True)
