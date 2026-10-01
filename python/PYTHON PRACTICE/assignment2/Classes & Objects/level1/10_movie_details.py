class Movie:
    def __init__(self, name, hero, heroine, rating):
        self.name = name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating


movies = [
    Movie("First Film", "Arun", "Meena", 4.2),
    Movie("Second Film", "Kiran", "Latha", 4.5),
]
for movie in movies:
    print(movie.name, movie.hero, movie.heroine, movie.rating)