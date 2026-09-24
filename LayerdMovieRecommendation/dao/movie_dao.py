from database.connection import Database
from model.movie import Movie

class MovieDao:

    def save_movie(self, movie):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = "insert into movies(title, genre, rating, release_year) values (%s, %s, %s, %s)" 

        data = (movie.title, movie.genre, movie.rating, movie.release_year)
        cursor.execute(query, data)

        cursor.close()
        conn.commit()
        conn.close()

        print("data saved successfully")


       
