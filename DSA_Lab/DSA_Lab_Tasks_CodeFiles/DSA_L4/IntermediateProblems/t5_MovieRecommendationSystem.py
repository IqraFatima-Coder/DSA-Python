class MovieNode:
    def __init__(self, movie_name, rating):
        self.movie_name = movie_name
        self.rating = rating
        self.next = None

class MovieRecommendationSystem:
    def __init__(self):
        self.head = None

    def add_movie(self, movie_name, rating):
        new_movie = MovieNode(movie_name, rating)
        if not self.head:
            self.head = new_movie
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_movie
        print(f'Movie "{movie_name}" with rating {rating} added.')

    def recommend_movies(self, min_rating):
        temp = self.head
        found = False
        print(f"Movies with rating greater than or equal to {min_rating}:")
        while temp:
            if temp.rating >= min_rating:
                print(f'- {temp.movie_name} - Rating: {temp.rating}')
                found = True
            temp = temp.next
        if not found:
            print("No movies found with the specified rating.")

# Example Usage
movie_system = MovieRecommendationSystem()
movie_system.add_movie("Inception", 4.8)
movie_system.add_movie("Titanic", 4.5)
movie_system.add_movie("Avatar", 4.7)

movie_system.recommend_movies(4.7)
