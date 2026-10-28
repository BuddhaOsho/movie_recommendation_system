import pandas as pd
import requests
import joblib
import os

API_KEY = "5a09e3d52cdaac15b09813c3f2c185c9"

movies = []

for page in range(1, 251):  # 250 pages × 20 records = ~5000 records

    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page={page}"

    response = requests.get(url, verify=False)

    if response.status_code == 200:

        data = response.json()

        for movie in data["results"]:
            movies.append({
                "ID": movie["id"],
                "Movie Title": movie["title"],
                "Original Title": movie["original_title"],
                "Overview": movie["overview"],
                "Adult": movie["adult"],
                "Release Date": movie["release_date"],
                "Rating": movie["vote_average"],
                "Popularity": movie["popularity"],
                "Vote Count": movie["vote_count"],
                "Original Language": movie["original_language"]
            })

        print(f"Page {page} collected")

    else:
        print(f"Failed on page {page}")
        break

df = pd.DataFrame(movies)

print(f"Total Records: {len(df)}")

df.to_csv("tmdb_movies.csv", index=False)

os.makedirs("artifacts", exist_ok=True)
joblib.dump(df, "artifacts/tmdb_movies.joblib")

print("Files saved successfully!")