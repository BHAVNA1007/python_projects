from dao.movie_dao import MovieDao


class MovieService:

    def save_movie(self, movie):

        movie_dao = MovieDao()
        movie_dao.save_movie(movie)

    def get_all_movies(self):

        movie_dao = MovieDao()
        rows = movie_dao.get_all_movies()
        return rows

    def search_movie_by_title(self,title):

        movie_dao = MovieDao()
        rows = movie_dao.search_movie_by_title(title)
        return rows

    def update_title_by_id(self, title, movie_id):

        movie_dao = MovieDao()
        update_count = movie_dao.update_title_by_id(title, movie_id)
        return update_count

    def delete_movie_by_id(self, movie_id):

        movie_dao = MovieDao()
        delete_count = movie_dao.delete_movie_by_id(movie_id)
        return delete_count
    
    
        