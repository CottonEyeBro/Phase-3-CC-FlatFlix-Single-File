class Movie:
    def __init__(self, title):
        self.title = title

        self._reviews = []
        self._reviewers = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0:
            self._title = title
        else:
            raise Exception

    def reviews(self):
        return self._reviews

    def reviewers(self):
        return list(set(self._reviewers))

    def average_rating(self):
        if self._reviews:
            avg_rating = sum([review.rating for review in self._reviews]) / len(self._reviews)
            return round(avg_rating, 1)
        else:
            return None
    






class Review:

    all = []

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

        self.viewer._reviews.append(self)
        self.viewer._reviewed_movies.append(self.movie)

        self.movie._reviews.append(self)
        self.movie._reviewers.append(self.viewer)

        Review.all.append(self)

    # Viewer property
    @property
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer(self, viewer):
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception

    # Movie property
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception

    # Rating
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if type(rating) == int and 1 <= rating <= 5 and not hasattr(self, "rating"):
            self._rating = rating
        else:
            raise Exception
        






class Viewer:
    def __init__(self, username):
        self.username = username

        self._reviews = []
        self._reviewed_movies = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if type(username) == str and 6 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception

    def reviews(self):
        return self._reviews

    def reviewed_movies(self):
        return list(set(self._reviewed_movies))

    def has_reviewed_movie(self, movie):
        if movie in self.reviewed_movies():
            return True
        else:
            return False

    def add_review(self, movie, rating):
        return Review(self, movie, rating)