from database.connection import Database


class MovieDao:

    def save_movie(self, movie):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = """
            INSERT INTO movies
            (title, genre, rating, release_year)
            VALUES (%s, %s, %s, %s)
        """

        data = (
            movie.title,
            movie.genre,
            movie.rating,
            movie.release_year
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()

        print("Movie saved successfully")

    def get_all_movies(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = "SELECT * FROM movies"

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows

    def search_movie_by_title(self,title):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = "select * from movies where title = %s "
        cursor.execute(query, (title,))

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows

    def update_title_by_id(self, title, movie_id):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'update movies set title = %s where movie_id = %s'
        cursor.execute(query, (title, movie_id))

        update_count = cursor.rowcount

        conn.commit()

        if update_count > 0:
            print("title updated successfully")
        else:
            print("id not found")

        cursor.close()
        conn.close()
        return update_count   

    def delete_movie_by_id(self, movie_id):
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'delete from movies where movie_id = %s'

        cursor.execute(query, (movie_id,))
        delete_count = cursor.rowcount
        conn.commit()

        if delete_count > 0:
            print(f"{delete_count}: movie deleted successfully")
        else:
            print("movie not found") 

        cursor.close()
        conn.close()
        return delete_count