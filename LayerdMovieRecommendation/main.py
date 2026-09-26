






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