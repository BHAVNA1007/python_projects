"""
main file
"""
from movie_recommendation.dashboard import show_dashboard
from movie_recommendation.recommendation import recommend_movies
from movie_recommendation.searchmovie import search_menu
from movie_recommendation.utils import display_loading_screen, display_main_menu, get_user_choice
from movie_recommendation.watchlist import watchlist_menu

class MovieRecommendation:

    def __init__(self):
        self.watchlist = []

    def run(self):
        """run program"""

        display_loading_screen()

        while True:

            display_main_menu()

            choice = get_user_choice()

            if choice == 1:

                show_dashboard(self.watchlist)

            elif choice == 2:
                search_menu()

            elif choice == 3:
                watchlist_menu(self.watchlist) 

            elif choice == 4:
                recommend_movies()

            elif choice == 5:
                print("\nThank you for using movie recommendation programmm...")  
                break
            else:
                print("Invalid choice. please try again.")

def main():
    """ start  program """   

    start = MovieRecommendation()
    start.run()

if __name__ == "__main__":
    main()               

