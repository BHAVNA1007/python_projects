"""
this module display the dashboard of movie Recommendation
"""

from movie_recommendation.moviedata import get_movie_list

LINE = "*" * 40

def show_dashboard(watchlist):
    """ it will display movie statistics."""

    movies = get_movie_list()

    total_movies = len(movies)
    watchlist_count =  len(watchlist)

    genre_count = {

        "Sci-Fi": 0,
        "Action": 0,
        "Comedy": 0,
        "Drama": 0,
        "Romance": 0,
        "Horror": 0
    }

    for movie in movies:
        genre_count[movie.genre] += 1

    print("\n")

    print(LINE)
    print("          DASHBOARD")
    print(LINE)
    
    print(f"Total Movies   : {total_movies}")
    print(f"Sci-fi Movies  : {genre_count["Sci-Fi"]}")
    print(f"Action Movies  : {genre_count["Action"]}")
    print(f"Comedy Movies  : {genre_count["Comedy"]}")
    print(f"Drama Movies   : {genre_count['Drama']}")
    print(f"Romance Movies : {genre_count['Romance']}")
    print(f"Horror Movies  : {genre_count['Horror']}")
    print(f"Watchlist Movies : {watchlist_count}")

print(LINE)


                  
