from model.user import User
from service.user_service import UserService

from model.watchlist import Watchlist
from service.watchlist_service import WatchlistService

from model.movie import Movie
from service.movie_service import MovieService

from service.recommendation_service import RecommendationService

from utils.validators import validate_id
from utils.validators import validate_required
from utils.validators import validate_rating
from utils.validators import validate_release_year
from utils.validators import validate_choice
from utils.validators import validate_status


while True:

    print("""========== MOVIE RECOMMENDATION SYSTEM ==========

1. User Management
2. Movie Management
3. Watchlist
4. Recommendations
5. Exit

    """)

    choice = input("Enter your choice: ")

    if not validate_choice(choice, 1, 5):
        print("Invalid choice")
        continue

    choice = int(choice)

    match choice:

        # ================= USER MANAGEMENT =================

        case 1:
            print("""========== USER MANAGEMENT ==========

1. Register User
2. Login User
3. Get User by ID
4. Update User
5. Delete User
6. Back

            """)

            user_choice = input("Enter your choice: ")

            if not validate_choice(user_choice, 1, 6):
                print("Invalid user menu choice")
                continue

            user_choice = int(user_choice)

            match user_choice:

                case 1:
                    print("========== REGISTER USER ==========")

                    name = input("Enter name: ")

                    if not validate_required(name):
                        print("User name cannot be empty")
                        continue

                    email = input("Enter email: ")

                    if not validate_required(email):
                        print("User email cannot be empty")
                        continue

                    password = input("Enter password: ")

                    if not validate_required(password):
                        print("User password cannot be empty")
                        continue

                    user = User(None, name, email, password)

                    user_service = UserService()
                    user_service.save_user(user)

                case 2:
                    print("========== LOGIN USER ==========")

                    email = input("Enter email: ")

                    if not validate_required(email):
                        print("User email cannot be empty")
                        continue

                    password = input("Enter password: ")

                    if not validate_required(password):
                        print("User password cannot be empty")
                        continue

                    user_service = UserService()
                    user = user_service.login_user(email, password)

                    if user:
                        print("Login successful")
                        print("Welcome,", user[1])
                    else:
                        print("Invalid email or password")

                case 3:
                    print("========== GET USER BY ID ==========")

                    user_id = input("Enter user id: ")

                    if not validate_id(user_id):
                        print("Invalid user id")
                        continue

                    user_id = int(user_id)

                    user_service = UserService()
                    user = user_service.get_user_by_id(user_id)

                    if user:
                        print("\nUser Details")
                        print("------------")
                        print("User ID:", user[0])
                        print("Name:", user[1])
                        print("Email:", user[2])
                    else:
                        print("User not found")

                case 4:
                    print("========== UPDATE USER ==========")

                    user_id = input("Enter user id: ")

                    if not validate_id(user_id):
                        print("Invalid user id")
                        continue

                    user_id = int(user_id)

                    name = input("Enter new name: ")

                    if not validate_required(name):
                        print("Name cannot be empty")
                        continue

                    user_service = UserService()

                    update_count = user_service.update_name_by_id(
                        user_id,
                        name
                    )

                    if update_count > 0:
                        print("User updated successfully")
                    else:
                        print("User not found")

                case 5:
                    print("========== DELETE USER ==========")

                    user_id = input("Enter user id: ")

                    if not validate_id(user_id):
                        print("Invalid user id")
                        continue

                    user_id = int(user_id)

                    user_service = UserService()

                    delete_count = user_service.delete_user_by_id(
                        user_id
                    )

                    if delete_count > 0:
                        print("User deleted successfully")
                    else:
                        print("User not found")

                case 6:
                    continue

                case _:
                    print("Invalid user menu choice")

        # ================= MOVIE MANAGEMENT =================

        case 2:
            print("""========== MOVIE MANAGEMENT ==========

1. Add Movie
2. View Movies
3. Search Movie
4. Update Movie
5. Delete Movie
6. Back

    """)

            movie_choice = input("Enter your choice: ")

            if not validate_choice(movie_choice, 1, 6):
                print("Invalid movie menu choice")
                continue

            movie_choice = int(movie_choice)

            match movie_choice:

                case 1:
                    print("========== ADD MOVIE ==========")

                    title = input("Enter movie title: ")

                    if not validate_required(title):
                        print("Movie title cannot be empty")
                        continue

                    genre = input("Enter genre: ")

                    if not validate_required(genre):
                        print("Genre cannot be empty")
                        continue

                    rating = input("Enter rating: ")

                    if not validate_rating(rating):
                        print("Invalid rating. Enter a value between 0 and 10")
                        continue

                    rating = float(rating)

                    release_year = input("Enter release year: ")
                    
                    if not validate_release_year(release_year):
                        print("Invalid release year")
                        continue
                    
                    release_year = int(release_year)

                    movie = Movie(
                        None,
                        title,
                        genre,
                        rating,
                        release_year
                    )

                    movie_service = MovieService()
                    movie_service.save_movie(movie)

                case 2:
                    print("========== VIEW MOVIES ==========")

                    movie_service = MovieService()
                    movies = movie_service.get_all_movies()

                    if movies:
                        for movie in movies:
                            print("\nMovie ID:", movie[0])
                            print("Title:", movie[1])
                            print("Genre:", movie[2])
                            print("Rating:", movie[3])
                            print("Release Year:", movie[4])
                    else:
                        print("No movies found")

                case 3:
                    print("========== SEARCH MOVIE ==========")

                    title = input("Enter movie title: ")

                    if not validate_required(title):
                        print("Title cannot be empty")
                        continue

                    movie_service = MovieService()
                    movies = movie_service.search_movie_by_title(title)

                    if movies:
                        for movie in movies:
                            print("\nMovie ID:", movie[0])
                            print("Title:", movie[1])
                            print("Genre:", movie[2])
                            print("Rating:", movie[3])
                            print("Release Year:", movie[4])
                    else:
                        print("Movie not found")

                case 4:
                    print("========== UPDATE MOVIE ==========")

                    movie_id = input("Enter movie id: ")

                    if not validate_id(movie_id):
                        print("Invalid movie id")
                        continue

                    movie_id = int(movie_id)

                    title = input("Enter new title: ")

                    if not validate_required(title):
                        print("Movie title cannot be empty")
                        continue

                    movie_service = MovieService()

                    update_count = movie_service.update_title_by_id(
                        title,
                        movie_id
                    )

                    if update_count > 0:
                        print("Movie updated successfully")
                    else:
                        print("Movie not found")

                case 5:
                    print("========== DELETE MOVIE ==========")

                    movie_id = input("Enter movie id: ")

                    if not validate_id(movie_id):
                        print("Invalid movie id")
                        continue

                    movie_id = int(movie_id)

                    movie_service = MovieService()

                    delete_count = movie_service.delete_movie_by_id(
                        movie_id
                    )

                    if delete_count > 0:
                        print("Movie deleted successfully")
                    else:
                        print("Movie not found")

                case 6:
                    continue

                case _:
                    print("Invalid movie menu choice")

        # ================= WATCHLIST =================

        case 3:
            print("""========== WATCHLIST ==========

1. Add to Watchlist
2. View Watchlist
3. Update Status
4. Remove from Watchlist
5. Back

    """)

            watchlist_choice = input("Enter your choice: ")

            if not validate_choice(watchlist_choice, 1, 5):
                print("Invalid user menu choice")
                continue

            watchlist_choice = int(watchlist_choice)

            match watchlist_choice:

                case 1:
                    print("========== ADD TO WATCHLIST ==========")

                    user_id = input("Enter user id: ")

                    if not validate_id(user_id):
                        print("Invalid user id")
                        continue

                    user_id = int(user_id)

                    movie_id = input("Enter movie id: ")

                    if not validate_id(movie_id):
                        print("Invalid movie id")
                        continue

                    movie_id = int(movie_id)

                    status = input("Enter status: ")

                    if not validate_status(status):
                        print("Invalid status. Use 'Want to Watch' or 'Watched'")
                        continue
                    
                    watchlist = Watchlist(
                        None,
                        user_id,
                        movie_id,
                        status
                    )

                    watchlist_service = WatchlistService()
                    watchlist_service.save_in_watchlist(
                        watchlist
                    )

                case 2:
                    print("========== VIEW WATCHLIST ==========")

                    user_id = input("Enter user id: ")

                    if not validate_id(user_id):
                        print("Invalid user id")
                        continue

                    user_id = int(user_id)

                    watchlist_service = WatchlistService()
                    movies = watchlist_service.get_watchlist(
                        user_id
                    )

                    if movies:
                        for movie in movies:
                            print("\nMovie ID:", movie[0])
                            print("Title:", movie[1])
                            print("Genre:", movie[2])
                            print("Rating:", movie[3])
                            print("Release Year:", movie[4])
                            print("Status:", movie[5])
                    else:
                        print("Watchlist is empty")

                case 3:
                    print("========== UPDATE WATCHLIST STATUS ==========")

                    user_id = input("Enter user id: ")

                    if not validate_id(user_id):
                        print("Invalid user id")
                        continue

                    user_id = int(user_id)

                    movie_id = input("Enter movie id: ")

                    if not validate_id(movie_id):
                        print("Invalid movie id")
                        continue

                    movie_id = int(movie_id)

                    status = input("Enter new status: ")

                    if not validate_required(status):
                        print("Status cannot be empty")
                        continue

                    watchlist_service = WatchlistService()

                    update_count = watchlist_service.update_status(
                        user_id,
                        movie_id,
                        status
                    )

                    if update_count > 0:
                        print("Status updated successfully")
                    else:
                        print("Watchlist record not found")

                case 4:
                    print("========== REMOVE FROM WATCHLIST ==========")

                    watchlist_id = input(
                        "Enter watchlist id: "
                    )

                    if not validate_id(watchlist_id):
                        print("Invalid watchlist id")
                        continue

                    watchlist_id = int(watchlist_id)

                    watchlist_service = WatchlistService()

                    delete_count = (
                        watchlist_service.remove_from_watchlist(
                            watchlist_id
                        )
                    )

                    if delete_count > 0:
                        print("Movie removed from watchlist")
                    else:
                        print("Watchlist record not found")

                case 5:
                    continue

                case _:
                    print("Invalid watchlist menu choice")

        # ================= RECOMMENDATIONS =================

        case 4:
            print("========== RECOMMENDATIONS ==========")

            user_id = input("Enter user id: ")

            if not validate_id(user_id):
                print("Invalid user id")
                continue

            user_id = int(user_id)

            recommendation_service = RecommendationService()

            recommendations = (
                recommendation_service.get_recommendations(
                    user_id
                )
            )

            if recommendations:
                print("\nRecommended Movies")
                print("------------------")

                for movie in recommendations:
                    print("Movie ID:", movie[0])
                    print("Title:", movie[1])
                    print("Genre:", movie[2])
                    print("Rating:", movie[3])
                    print("Release Year:", movie[4])
                    print()
            else:
                print("No recommendations found")

        # ================= EXIT =================

        case 5:
            print(
                "Thank you for using Movie Recommendation System."
            )
            break

        case _:
            print("Invalid choice")                         






#from model.movie import Movie
#from service.movie_service import MovieService

'''
from service.recommendation_service import RecommendationService

recommendation_service = RecommendationService()




user_id = int(input("Enter user id: "))

recommendations = recommendation_service.get_recommendations(user_id)

#for movie in recommendations:
#print("\nRecommended Movies")

print("\nRecommended Movies")
print("------------------")

for movie in recommendations:
    print("Movie ID:", movie[0])
    print("Title:", movie[1])
    print("Genre:", movie[2])
    print("Rating:", movie[3])
    print("Release Year:", movie[4])
    print()
'''


'''
from model.watchlist import Watchlist

from service.watchlist_service import WatchlistService

watchlist_service = WatchlistService()

user_id = int(input("Enter user id: "))
movie_id = int(input("Enter movie id: "))
status = input("Enter new status: ")

update_count = watchlist_service.update_status(user_id, movie_id, status)

if update_count > 0:
    print("Status updated successfully")
else:
    print("Watchlist record not found")
'''
    

'''
user_id = int(input("Enter user id: "))
movie_id = int(input("Enter movie id: "))
status = input("Enter status: ")

watchlist = Watchlist(None, user_id, movie_id, status)

watchlist_service = WatchlistService()
watchlist_service.save_in_watchlist(watchlist)
'''

'''
id = int(input("Enter user id: "))

view = watchlist_service.get_watchlist(id)

for movie in view:
    print(movie)
'''


'''
#case 1:
watchlist = Watchlist(None, 1, 1)
watchlist_service.save_in_watchlist(watchlist)
'''


#from service.user_service import UserService

# case 5:
'''
delete_count = UserService()
user_id = int(input("Enter user id which user you want to delete: "))
print(delete_count.delete_user_by_id(user_id))
'''
#Enter user id which user you want to delete: 2
#2 : deleted successfully
#1



#case 4:
'''
update_count = UserService()
user_id = int(input("Enter user id which you want to update: "))
user_name = input("enter new name: ")

print(update_count.update_user_by_id(user_name, user_id))
'''
#Enter user id which you want to update: 2
#enter new name: Priyanka
#Priyanka: user name updated successfully
#1




#case 3
'''
user = UserService()
id = int(input("enter user id: "))
print(user.get_user_by_id(id))
'''

'''
case 2
email = input("enter user email:  ")
password = input("enter user password:  ")

user = UserService()
print(user.login_user(email, password)) 
'''



'''
from model.user import User
case 1
user = User(None, "Rahul", 'rahul@gamil.com', 'abc123')
user_service = UserService()
user_service.save_user(user)

print(user.user_id)
print(user.name)
print(user.email)
print(user.password)
'''



#========================================================
'''
#case 5

movie_service = MovieService()
id = int(input("enter movie id: "))
delete_count = movie_service.delete_movie_by_id(id)
'''

'''
# case 4

id = int(input("Enter movie id: "))
title = input("Enter new title: ")

movie_service = MovieService()
count = movie_service.update_title_by_id(title, id)

'''

'''
# case 3
title = input("Enter movie name: ")

movie_service = MovieService()
movies = movie_service.search_movie_by_title(title)
for movie in movies:
    print(movie)
'''

#case 2
'''
movie_service = MovieService()
movies = movie_service.get_all_movies()

for movie in movies:
    print(movie)
'''
'''
case 1

movie = Movie(
    None,
    "Inception",
    "Sci-Fi",
    8.8,
    2010
)

movie_service = MovieService()
movie_service.save_movie(movie)
'''



'''
from database.connection import Database
from service.movie_service import MovieService

db = Database()
conn = db.connect()

if conn.is_connected():
    print("database connected successfully")
conn.close()

movie = MovieService()
'''


'''
from model.movie import Movie


movie = Movie(1, "Interstellar", "Sci-Fi", 8.7, 2014)

print(movie.movie_id)
print(movie.title)
print(movie.genre)
print(movie.rating)
print(movie.release_year)


database connected successfully
1
Interstellar
Sci-Fi
8.7
2014

'''

'''

from model.user import User

user = User(1, "Rahul", 'rahul@gamil.com', 'abc123')

print(user.user_id)
print(user.name)
print(user.email)
print(user.password)

database connected successfully
1
Rahul
rahul@gamil.com
abc123
'''

'''
from model.watchlist import Watchlist

watchlist = Watchlist(1,2,5)

print(watchlist.user_id)
print(watchlist.movie_id)
print(watchlist.watchlist_id)

database connected successfully
2
5
1

'''
'''

from model.movie import Movie
from dao.movie_dao import MovieDao

movie = Movie(
    None,
    "Interstellar",
    "Sci-Fi",
    8.7,
    2014
)

movie_dao = MovieDao()
movie_dao.save_movie(movie)
'''