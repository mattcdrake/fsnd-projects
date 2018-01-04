def read_text():
    quotes = open("movie_quotes.txt")
    content = quotes.read()
    print(content)
    quotes.close()

read_text()
