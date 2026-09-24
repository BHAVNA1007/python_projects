from model.movie import Movie
from service.movie_service import MovieService



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