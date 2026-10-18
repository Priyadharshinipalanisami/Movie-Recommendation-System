from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/movies.csv")
print("DATASET SHAPE:", df.shape)
print("\\nCOLUMNS:", list(df.columns))
print("\\nDATA TYPES:\\n", df.dtypes)
print("\\nMISSING VALUES BEFORE CLEANING:\\n", df.isna().sum())
print("\\nDUPLICATE TITLES:", df["title"].duplicated().sum())
print("\\nSAMPLE DATA:\\n", df.head().to_string(index=False))
genres = df["genres"].fillna("").str.split("|").explode().str.strip()
counts = genres[genres.ne("")].value_counts().head(15)
print("\\nGENRE COUNTS:\\n", counts.to_string())
if not counts.empty:
    counts.sort_values().plot(kind="barh", figsize=(9, 5), title="Most Common Genres")
    plt.xlabel("Movie count")
    plt.tight_layout()
    plt.savefig("genre_distribution.png", dpi=150)
    print("\\nSaved genre_distribution.png")
