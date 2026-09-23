from database.connection import Database

db = Database()
conn = db.connect()

if conn.is_connected():
    print("database connected successfully")


conn.close()




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