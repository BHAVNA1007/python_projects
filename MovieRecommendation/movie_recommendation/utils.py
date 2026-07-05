"""
module contains utility functions used throughout the movie recommendation.
"""
import winsound
import time

LINE = "*" * 40

def display_loading_screen():
    """Display the loading screen."""

    print(LINE)
    print("     MOVIE RECOMMENDATION")
    print(LINE)

    loading_messages = [

        "Loading Movies...",
        "Loading Search Module...",
        "Loading Watchlist...",
        "Loading Recommendations..."
    ]

    for message in loading_messages:
        print(message)
        time.sleep(1)
        winsound.Beep(500, 500)

    print("\nLoading Complete :)") 
    
    print("\nWelcome to movie Recommendation App!")  
    print(LINE)

def display_main_menu():
    """Display the main menu."""

    print("\n")
    print(LINE)
    print("    MAIN MENU")
    print(LINE)

    print("1. Dashboard")
    print("2. Search Movie")
    print("3. Watchlist")
    print("4. Recommendation")
    print("5. Exit")
    print(LINE)

def get_user_choice():
    """Get the user's menu choice"""

    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        
        except ValueError:
            print("Enter a valid choice.")

def press_enter():
    """pause the program until the user presses Enter."""

    input("\nPress Enter to continue...") 






