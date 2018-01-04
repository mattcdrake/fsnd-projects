import media
import urllib.request
import webbrowser

the_fountain = media.Movie("The Fountain", "Hugh Jackman tries to find "
                           "the cure for cancer.", 
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU5OTczMTcxMV5BMl5BanBnXkFtZTcwNDg3MTEzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg", 
                           "https://www.youtube.com/watch?v=dAuxryJ6pv8")

print(the_fountain.title)

url = the_fountain.trailer_youtube_url

webbrowser.open(url)
