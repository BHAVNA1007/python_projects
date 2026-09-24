
from dao.movie_dao import MovieDao

class MovieService:

    def save_movie(self, movie):
        movie_dao = MovieDao()
        movie_dao.save_movie(movie)
       

