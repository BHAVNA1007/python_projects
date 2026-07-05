

"""
This module stores movie information for the movie recommendation.
"""

class Movie:
    """Represent a movie."""

    def __init__(self, name, genre, year, rating):
        """movie details."""

        self.name = name
        self.genre = genre
        self.year = year
        self.rating = rating

movie_list = [
    Movie("Interstellar", "Sci-Fi", 2014, 4.8),
    Movie("Inception", "Sci-Fi", 2010, 4.8),
    Movie("Avatar", "Sci-Fi", 2009, 4.6),
    Movie("The Martian", "Sci-Fi", 2015, 4.5),
    Movie("Arrival", "Sci-Fi", 2016, 4.4),

    Movie("Titanic", "Romance", 1997, 4.7),
    Movie("The Notebook", "Romance", 2004, 4.4),
    Movie("La La Land", "Romance", 2016, 4.3),
    Movie("Me Before You", "Romance", 2016, 4.2),
    Movie("A Walk to Remember", "Romance", 2002, 4.5),

    Movie("John Wick", "Action", 2014, 4.6),
    Movie("Mad Max: Fury Road", "Action", 2015, 4.7),
    Movie("Gladiator", "Action", 2000, 4.8),
    Movie("Extraction", "Action", 2020, 4.3),
    Movie("The Dark Knight", "Action", 2008, 4.9),

    Movie("The Conjuring", "Horror", 2013, 4.5),
    Movie("Insidious", "Horror", 2010, 4.3),
    Movie("The Nun", "Horror", 2018, 4.0),
    Movie("It", "Horror", 2017, 4.2),
    Movie("Annabelle", "Horror", 2014, 4.0),

    Movie("3 Idiots", "Comedy", 2009, 4.9),
    Movie("PK", "Comedy", 2014, 4.7),
    Movie("Golmaal", "Comedy", 2006, 4.2),
    Movie("Hera Pheri", "Comedy", 2000, 4.8),
    Movie("Bhool Bhulaiyaa", "Comedy", 2007, 4.5),

    Movie("The Shawshank Redemption", "Drama", 1994, 4.9),
    Movie("Forrest Gump", "Drama", 1994, 4.8),
    Movie("The Pursuit of Happyness", "Drama", 2006, 4.7),
    Movie("Whiplash", "Drama", 2014, 4.8),
    Movie("The Green Mile", "Drama", 1999, 4.8)
]


def get_movie_list():
    """Return the list of movies."""

    return movie_list