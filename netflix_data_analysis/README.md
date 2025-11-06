# 🎬 Netflix Data Analysis (via TMDB API)
# 📘 Overview

This project analyzes trending movies and TV shows using **The Movie Database (TMDB) API, similar to Netflix-style data insights.**
It fetches live data, cleans and processes it with Pandas, and visualizes top trends using Matplotlib.

This is my third GitHub project, created to strengthen my skills in working with APIs, JSON, and Data Visualization.

# 🧩 Features

✅ Fetches real-time trending movies and shows from TMDB
✅ Converts complex JSON into a structured Pandas DataFrame
✅ Analyzes Top 10 most popular and Top 10 highest-rated titles
✅ Exports data into a CSV file
✅ Generates and saves bar charts for visual representation

# 🧠 Tech Stack

Python 3.10+

Pandas – for data analysis

Matplotlib – for data visualization

Requests – for API data fetching

TMDB API – for live trending content

## ⚙️ How to Run
1️⃣ Clone this Repository
git clone https://github.com/<your-username>/netflix_data_analysis.git
cd netflix_data_analysis

2️⃣ Install Dependencies
pip install pandas matplotlib requests

3️⃣ Add Your TMDB API Key

Open netflix_analysis.py

Find this line:

API_KEY = "YOUR_API_KEY"


Replace "YOUR_API_KEY" with your actual TMDB API key from the TMDB Developer Portal
.

4️⃣ Run the Script
python netflix_analysis.py


📊 Example Output
Chart	Description
🎬 Top 10 Trending Movies	Most popular titles of the day
⭐ Top 10 Highest Rated	Highest-rated movies and shows

🧠 Key Learnings

How to work with APIs and JSON data

How to use Pandas for real-time data analysis

How to create and save visualizations using Matplotlib

Building end-to-end projects suitable for GitHub portfolios and internships

📂 Project Structure
📦 netflix_data_analysis
 ┣ 📜 netflix_analysis.py
 ┣ 📊 tmdb_trending.csv
 ┣ 🖼️ Top_10_Trending_Movies.png
 ┣ 🖼️ Top_10_Highest_Rated_Movies.png
 ┗ 📄 README.md

💼 Author

Yunus
🚀 Data Science & AI Enthusiast | Focused on Real-World AI & Analytics Projects