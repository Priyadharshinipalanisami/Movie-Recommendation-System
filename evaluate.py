from recommender import MovieRecommender

engine = MovieRecommender()
queries = ["Toy Story", "The Matrix", "Finding Nemo", "The Dark Knight", "Titanic", "Dune"]
print(f"Qualitative evaluation on {len(engine.movies)} movies")
for query in queries:
    print("\\n" + "=" * 65 + "\\nQUERY:", query)
    results = engine.recommend(query, 5)
    if not results:
        print("No results")
    for rank, item in enumerate(results, 1):
        print(f'{rank}. {item["title"]} | score={item["similarity"]:.3f} | {item["genres"]}')
