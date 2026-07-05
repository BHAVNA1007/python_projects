"""
this module manage the watchlist.
"""
import winsound
from movie_recommendation.moviedata import get_movie_list
from movie_recommendation.utils import LINE, press_enter

def watchlist_menu(watchlist):
    """Display the watchlist menu"""

    while True:

        print("\n")
        print(LINE)
        print("      WATCHLIST MENU")
        print(LINE)
        print("\n1. view watchlist")
        print("2. add movie")
        print("3. Remove movie")
        print("4. back")
        print(LINE)

        try: 
            choice = int(input("Enter your choice: "))
        except ValueError:

            winsound.Beep(1000, 300)
            print('Please Enter a valid choice.')
            continue

        if choice == 1:
            view_watchlist(watchlist)

        elif choice == 2:
            add_movie(watchlist)

        elif choice == 3:
            remove_movie(watchlist)

        elif choice == 4:
            break
        else:
            print("Invalid choice.")


def view_watchlist(watchlist):
    """Display all movies in the watvhlist. """

    print("\n")
    print(LINE)
    print("        MY WATCHLIST")
    print(LINE)

    if len(watchlist) == 0:
        print("your watchlist is empty.")
    else:
        for  i, movie in enumerate(watchlist, start=1):
            print(f"{i}.{movie.name} ({movie.genre})")

        print(LINE)
        press_enter()

def add_movie(watchlist):
    """add a movie to the watchlist."""

    movies = get_movie_list()

    movie_name = input("\nEnter movie name: ").strip().lower() 

    for watched in watchlist:
        if watched.name.lower() == movie_name:
            print("Movie is already in your watchlist.")
            press_enter()
            return
    for movie in movies:
        if movie.name.lower() == movie_name:
            watchlist.append(movie)
            print(f"{movie.name} added") 
            winsound.Beep(20000, 3000)
            press_enter()
            return

    print("movie not found.")
    press_enter()

def remove_movie(watchlist):
    """Remove a movie from the watchlist"""

    if len(watchlist) == 0:
        print("\nYour watchlist is empty.")
        press_enter()
        return

    movie_name = input("\nEnter movie name to remove: ").strip().lower()

    for movie in watchlist:

        if movie.name.lower() == movie_name:
            watchlist.remove(movie)
            print(f"{movie.name} removed")
            press_enter()
            return

    print("Movie not found in your watchlist.") 
    press_enter()              

