"""
this module contain all movie search functions.
"""

from movie_recommendation.moviedata import get_movie_list
from movie_recommendation.utils import LINE,  press_enter

def search_menu():
    """Display the search menu."""

    while True:

        print("\n")
        print(LINE)
        print("          SEARCH MENU")
        print(LINE)
        print("\n1. Search by Movie Name")
        print("2. Search by Genre")
        print("3. Back")
        print(LINE)

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            
            print("Please Enter a valid choice.....")    
            continue
        if choice == 1:
            search_by_name()

        elif choice == 2:
            search_by_genre()

        elif choice == 3:
           break
        else:
          
           print("Invalid choice.") 
             
def search_by_name():
    """search a movie using name. """

    movies = get_movie_list()

    search_name = input("\nEnter movie name: ").strip().lower()

    found = False

    for movie in movies:

        if movie.name.lower() == search_name:
              
            print("\nMovie Found")
            print(LINE)
            print(f"Name  : {movie.name}")
            print(f"Genre : {movie.genre}")
            print(f"Year  : {movie.year}")
            print(f"Rating: {movie.rating}")
            print(LINE)

            found = True
            break

    if not found:
        print("\nMovie not found.")

    press_enter()


def search_by_genre():
    """search movies by genre."""

    movies = get_movie_list()

    genre = input("\nEnter genre: ").strip().lower()

    found = False

    print("\nMovies")

    for movie in movies:

        if movie.genre.lower() == genre:

            print(f"  {movie.name}")

            found = True

    if not found:
        print("No movies found in this genre.")

    press_enter()                        
