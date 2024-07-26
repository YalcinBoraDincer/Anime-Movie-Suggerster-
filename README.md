# Anime and Movie Recommendation App

This project is a GUI application developed using PyQt5, providing users with anime and movie recommendations. It leverages the Jikan API for anime data and the TMDb API for movie data.

## Features

### Anime Recommendation

- **Random Anime:** Get details of a randomly selected anime.
- **Genre-based Recommendations:** View a list of anime based on selected genres.
- **Detailed Information:** Displays detailed information including title, genres, themes, episodes, status, score, rating, popularity, year, and synopsis.
- **User Interface:** The UI includes a main frame image, anime image, and detailed text description.

### Movie Recommendation

- **Top Rated Movies**
- **Top Rated Series**
- **Airing Today Series**
- **Popular Series**
- **Upcoming Movies**
- **Detailed Information:** Displays detailed information including title, release date, and genres.
- **User Interface:** The UI includes a main frame image, movie/series image, and detailed text description.

## Gif

![unknown_2024 07 26-21 24-ezgif com-speed](https://github.com/user-attachments/assets/b2f7b155-bb89-4e19-b13a-cf130fe9f6d9)



## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/AnimeMovieRecommendationApp.git
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main application:

    ```bash
    python main.py
    ```

2. Navigate through the UI to get anime or movie recommendations.

## API Keys

Ensure you have valid API keys for the Jikan API and TMDb API. You can obtain them from:
- [Jikan API](https://jikan.moe/)
- [TMDb API](https://www.themoviedb.org/)

Set the API keys in the respective files:
- `Anime.py` for Jikan API
- `Movie.py` for TMDb API



