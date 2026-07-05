"""
this module recommends movies based on genre>
"""

from movie_recommendation.moviedata import get_movie_list
from movie_recommendation.utils import LINE, press_enter

def recommend_movies():
    """recommend movies based on genre."""

    movies = get_movie_list()

    print("\n")
    print(LINE)
    print("   MOVIE RECOMMENDATION")
    print(LINE)

    genre = input("\nEnter your favorite genre: ").strip().lower()

    found = False

    print("\nRecommended movies\n")   

    for movie in movies:
        if movie.genre.lower() == genre:

            print(f"Movie  : {movie.name}")
            print(f"Genre  : {movie.genre}")
            print(f"Year   : {movie.year}")
            print(f"Rating : {movie.rating}")

            found = True

    if not found:

        print("Sorry! no recommendations found.")

    press_enter            