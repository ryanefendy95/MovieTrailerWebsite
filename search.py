"""
Search info. Search movie's ID and get the related information

"""
import requests
import json
import constants


class Search():
    """ This class provides a way to get a movie ID and search info about the
        movie
    """

    def __init__(self, url):
        self.url = url

    def get_id(self):
        # Get movie's id
        response = requests.get(self.url)
        movie_id = response.json()['results'][0]['id']
        return movie_id

    def search_movie_info(self):
        # Search movie info
        response = requests.get(self.url)
        # Create a JSON file with movie's info
        movie_json = {}
        movie_json['movie_title'] = response.json()['title']
        movie_json['movie_storyline'] = response.json()['overview']
        movie_json['poster_image'] = constants.IMAGE_URL.format (poster_path=response.json()['poster_path'])  # NOQA
        movie_json['trailer_youtube'] = constants.YOUTUBE_URL.format  (youtube_key=response.json()['videos']['results'][0]['key'])  # NOQA
        return json.dumps(movie_json)
