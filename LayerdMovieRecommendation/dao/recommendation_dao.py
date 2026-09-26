from database.connection import Database

class RecommendationDao:

     def get_recommendations(self, user_id):
          db = Database()
          conn = db.connect()
          cursor = conn.cursor()

          query ="""select * from movies where genre IN (select m.genre from movies m JOIN watchlist w ON m.movie_id = w.movie_id where w.user_id = %s) AND movie_id NOT IN (select movie_id from watchlist where user_id = %s)"""

          cursor.execute(query, (user_id, user_id))

          rows = cursor.fetchall()

          cursor.close()
          conn.close()

          return rows