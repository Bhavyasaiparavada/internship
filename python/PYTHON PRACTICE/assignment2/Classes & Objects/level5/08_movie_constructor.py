class Movie:
    def __init__(self, name, hero, heroine, rating):
        self.name = name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating

    def display(self):
        print(self.name, self.hero, self.heroine, self.rating)


movie = Movie("First Film", "Arun", "Meena", 4.2)
movie.display()