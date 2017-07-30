import media
import fresh_tomatoes

# create object/instance from Movie class
baby_driver = media.Movie("Baby Driver",
                    "After being coerced into working for a crime boss, a young getaway driver finds himself taking part in a heist doomed to fail.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM3MjQ1MzkxNl5BMl5BanBnXkFtZTgwODk1ODgyMjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                    "https://youtu.be/D9YZw_X5UzQ")

logan = media.Movie("Logan",
                    "In the near future, a weary Logan cares for an ailing Professor X, somewhere on the Mexican border. However, Logan's attempts to hide from the world, and his legacy, are upended when a young mutant arrives, pursued by dark forces.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQwODQwNTg4OV5BMl5BanBnXkFtZTgwMTk4MTAzMjI@._V1_.jpg",
                    "https://youtu.be/Div0iP65aZo")

spider_man = media.Movie("Spider-Man: Homecoming",
                        "Peter Parker, with the help of his mentor Tony Stark, tries to balance his life as an ordinary high school student in New York City while fighting crime as his superhero alter ego Spider-Man when a new threat emerges.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1_SY1000_CR0,0,658,1000_AL_.jpg",
                        "https://youtu.be/DiTECkLZ8HM")

movies = [baby_driver, logan, spider_man] # create list and add movies
fresh_tomatoes.open_movies_page(movies) # create html with list of movies