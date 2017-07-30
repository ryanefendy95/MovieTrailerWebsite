"""
Main script

"""
import json
import search
import media
import constants
import fresh_tomatoes


movies = []


def get_movie_list(movie_info, movies_list):
    """ Create a movie list with movie info
    """
    movie = media.Movie(movie_info['movie_title'],
                        movie_info['movie_storyline'],
                        movie_info['poster_image'],
                        movie_info['trailer_youtube'])
    movies_list.append(movie)


# For each movie get the id and the info until there are no more movies
for movie in constants.SEARCH_LIST:
    search_id = search.Search(constants.SEARCH_URL.format(api_key=constants.API_KEY, query=movie))
    movie_id = search_id.get_id() # get id

    search_info = search.Search(constants.INFO_URL.format(api_key=constants.API_KEY, movie_id=movie_id))
    movie_json = search_info.search_movie_info()

    get_movie_list(json.loads(movie_json), movies) # convert json to python dictionary

fresh_tomatoes.open_movies_page(movies)
