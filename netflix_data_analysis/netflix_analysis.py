# ============================================
# 🎬 Netflix Data Analysis (via TMDB API)
# Author: Yunus
# Description: Fetches trending movies/shows using TMDB API,
#              analyzes genres, popularity, and ratings visually.
# ============================================

import requests
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Fetch data from TMDB API
API_KEY = "YOUR_API_KEY"   # ← Replace with your actual key locally, keep hidden on GitHub
url = f"https://api.themoviedb.org/3/trending/all/day?api_key={API_KEY}"

response = requests.get(url)
data = response.json()

# Step 2: Convert JSON to DataFrame
df = pd.DataFrame(data["results"])

# Step 3: Keep important columns only
df = df[["title", "name", "media_type", "popularity", "vote_average", "vote_count"]]
df = df.rename(columns={"name": "show_name", "title": "movie_title"})

# Step 4: Handle missing values
df = df.fillna("N/A")

# Step 5: Save dataset locally
df.to_csv("tmdb_trending.csv", index=False)
print("✅ Data saved as tmdb_trending.csv")

# Step 6: Display summary
print("\n🎥 Top 5 Trending Titles:")
print(df.head(5)[["movie_title", "show_name", "media_type", "popularity"]])

# Step 7: Visualization — Top 10 by Popularity
top10 = df.sort_values(by="popularity", ascending=False).head(10)
plt.figure(figsize=(10, 5))
plt.barh(top10["movie_title"].fillna(top10["show_name"]), top10["popularity"], color="crimson")
plt.xlabel("Popularity", fontweight="bold")
plt.ylabel("Title", fontweight="bold")
plt.title("🔥 Top 10 Trending Movies/Shows on TMDB", fontsize=12, fontweight="bold", color="purple")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("Top_10_Trending_Movies.png", dpi=300)
plt.show()

# Step 8: Visualization — Top 10 by Rating
top_rated = df.sort_values(by="vote_average", ascending=False).head(10)
plt.figure(figsize=(10, 5))
plt.barh(top_rated["movie_title"].fillna(top_rated["show_name"]), top_rated["vote_average"], color="goldenrod")
plt.xlabel("Average Rating", fontweight="bold")
plt.ylabel("Title", fontweight="bold")
plt.title("⭐ Top 10 Highest Rated Movies/Shows", fontsize=12, fontweight="bold", color="darkgreen")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("Top_10_Highest_Rated_Movies.png", dpi=300)
plt.show()

# Step 9: Summary Statistics
print("\n📊 Overall Statistics:")
print(f"Average Popularity: {round(df['popularity'].mean(), 2)}")
print(f"Average Rating: {round(df['vote_average'].mean(), 2)}")
print(f"Average Votes: {round(df['vote_count'].mean(), 2)}")

print("\n✨ Analysis Complete! Visuals saved successfully.")
