import media
import urllib
import fresh_tomatoes

the_fountain = media.Movie("The Fountain", "Hugh Jackman tries to find "
                           "the cure for cancer.", 
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU5OTczMTcxMV5BMl5BanBnXkFtZTcwNDg3MTEzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg", 
                           "https://www.youtube.com/watch?v=dAuxryJ6pv8")

movies = [the_fountain]

# fresh_tomatoes.open_movies_page(movies)

for movie in movies:
    print(movie.__class__.__name__)