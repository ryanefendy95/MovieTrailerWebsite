"""
CONSTANTS

"""

# List of your favourites movies
SEARCH_LIST = ['baby driver',
               'logan',
               'spider-Man: homecoming']

# Your The Movie Database's API KEY
API_KEY = 'd71c97116bb8d496dedeb261fc96f759'

# URLs required to run script
SEARCH_URL = 'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}'
INFO_URL = 'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US&append_to_response=videos'
IMAGE_URL = 'http://image.tmdb.org/t/p/w342/{poster_path}'
YOUTUBE_URL = 'https://www.youtube.com/watch?v={youtube_key}'