# Question 8: Create a Movie class using __init__() and a method to display movie information.

class Movie:
    def __init__(self, title, director, release_year, genre, duration, rating):
        """Initialize movie attributes"""
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre
        self.duration = duration  # in minutes
        self.rating = rating  # out of 10
    
    def display_info(self):
        """Display complete movie information"""
        print(f"\n{'='*60}")
        print(f"MOVIE INFORMATION")
        print(f"{'='*60}")
        print(f"Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Genre: {self.genre}")
        print(f"Release Year: {self.release_year}")
        print(f"Duration: {self.duration} minutes ({self.duration//60} hrs {self.duration%60} mins)")
        print(f"Rating: {self.rating}/10")
        print(f"{'='*60}\n")
    
    def display_brief_info(self):
        """Display brief movie information"""
        duration_text = f"{self.duration//60}h {self.duration%60}m"
        print(f"{self.title:30} | {self.director:20} | {self.genre:15} | {self.rating}/10 | {duration_text}")
    
    def get_movie_age(self, current_year=2024):
        """Get the age of the movie"""
        age = current_year - self.release_year
        return age
    
    def get_rating_category(self):
        """Get rating category"""
        if self.rating >= 9:
            return "Masterpiece"
        elif self.rating >= 8:
            return "Excellent"
        elif self.rating >= 7:
            return "Great"
        elif self.rating >= 6:
            return "Good"
        elif self.rating >= 5:
            return "Average"
        else:
            return "Poor"
    
    def is_classic(self, classic_threshold=20):
        """Check if movie is a classic"""
        age = self.get_movie_age()
        return age >= classic_threshold
    
    def display_detailed_info(self):
        """Display detailed movie information with analysis"""
        print(f"\nTitle: {self.title}")
        print(f"Director: {self.director}")
        print(f"Released: {self.release_year} (Age: {self.get_movie_age()} years)")
        print(f"Genre: {self.genre}")
        print(f"Duration: {self.duration} minutes")
        print(f"Rating: {self.rating}/10 - {self.get_rating_category()}")
        if self.is_classic():
            print(f"Status: CLASSIC FILM ★")
        print("-" * 60)


# Create movie objects using __init__()
print("MOVIE DATABASE\n")

movie1 = Movie("The Shawshank Redemption", "Frank Darabont", 1994, "Drama", 142, 9.3)
movie2 = Movie("The Godfather", "Francis Ford Coppola", 1972, "Crime/Drama", 175, 9.2)
movie3 = Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi/Thriller", 148, 8.8)
movie4 = Movie("Interstellar", "Christopher Nolan", 2014, "Sci-Fi/Drama", 169, 8.6)
movie5 = Movie("Pulp Fiction", "Quentin Tarantino", 1994, "Crime/Drama", 154, 8.9)
movie6 = Movie("Avatar", "James Cameron", 2009, "Sci-Fi/Adventure", 162, 7.8)

# Display detailed information
print("DETAILED MOVIE INFORMATION")
print("=" * 60)
movie1.display_info()
movie2.display_info()
movie3.display_info()

# Display brief information
print("\nMOVIE LIST")
print("=" * 60)
print(f"{'Title':<30} | {'Director':<20} | {'Genre':<15} | {'Rating':<6} | {'Duration':<10}")
print("-" * 60)
movie1.display_brief_info()
movie2.display_brief_info()
movie3.display_brief_info()
movie4.display_brief_info()
movie5.display_brief_info()
movie6.display_brief_info()

# Display detailed analysis
print("\n\nDETAILED ANALYSIS")
print("=" * 60)
movie1.display_detailed_info()
movie2.display_detailed_info()
movie3.display_detailed_info()
movie4.display_detailed_info()
movie5.display_detailed_info()
movie6.display_detailed_info()

# Movie statistics
print("\n\nMOVIE STATISTICS")
print("=" * 60)
all_movies = [movie1, movie2, movie3, movie4, movie5, movie6]
average_rating = sum(m.rating for m in all_movies) / len(all_movies)
classics = sum(1 for m in all_movies if m.is_classic())

print(f"Total Movies: {len(all_movies)}")
print(f"Average Rating: {average_rating:.2f}/10")
print(f"Classic Films (20+ years): {classics}")
print(f"Highest Rated: {max(all_movies, key=lambda m: m.rating).title} ({max(all_movies, key=lambda m: m.rating).rating}/10)")
print(f"Lowest Rated: {min(all_movies, key=lambda m: m.rating).title} ({min(all_movies, key=lambda m: m.rating).rating}/10)")

# Average duration
avg_duration = sum(m.duration for m in all_movies) / len(all_movies)
print(f"Average Duration: {int(avg_duration)} minutes")

# Rating category breakdown
print("\n\nRATING CATEGORY BREAKDOWN")
print("=" * 60)
categories = {}
for movie in all_movies:
    category = movie.get_rating_category()
    categories[category] = categories.get(category, 0) + 1

for category, count in sorted(categories.items(), reverse=True):
    print(f"{category:<20}: {count} movie(s)")
