class Movie:
    def __init__(self, movie_name, hero, heroine, rating):
        self.movie_name = movie_name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating


movies = [
    Movie("Dangal", "Aamir Khan", "Fatima Sana Shaikh", 8.3),
    Movie("3 Idiots", "Aamir Khan", "Kareena Kapoor", 8.4),
]

for movie in movies:
    print("Movie:", movie.movie_name)
    print("Hero:", movie.hero)
    print("Heroine:", movie.heroine)
    print("Rating:", movie.rating)
    print()
