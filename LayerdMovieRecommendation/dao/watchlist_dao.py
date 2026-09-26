from model.watchlist import Watchlist
from database.connection import Database

class WatchListDao:

    def remove_from_watchlist(self, watchlist_id):
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()
    
        query = "DELETE FROM watchlist WHERE watchlist_id = %s"
    
        cursor.execute(query, (watchlist_id,))
    
        delete_count = cursor.rowcount
    
        conn.commit()
    
        cursor.close()
        conn.close()
    
        return delete_count

    def update_status(self, user_id, movie_id, status):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = "UPDATE watchlist SET status = %s WHERE user_id = %s AND movie_id = %s"

        cursor.execute(query, (status, user_id, movie_id))
    
        update_count = cursor.rowcount
    
        conn.commit()
    
        cursor.close()
        conn.close()
    
        return update_count


    def get_watchlist(self, user_id):
       db = Database()
       conn = db.connect()
       cursor = conn.cursor()
   
       query = "SELECT m.movie_id, m.title, m.genre, m.rating, m.release_year FROM watchlist w JOIN movies m ON w.movie_id = m.movie_id WHERE w.user_id = %s"
   
       cursor.execute(query, (user_id,))
       rows = cursor.fetchall()
   
       cursor.close()
       conn.close()
   
       return rows


    def save_in_watchlist(self, watchlist):
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()
    
        query = 'insert into watchlist (user_id, movie_id, status) values (%s, %s, %s)'
    
        data = (watchlist.user_id, watchlist.movie_id, watchlist.status)
    
        cursor.execute(query, data)
        conn.commit()
    
        cursor.close()
        conn.close()
    