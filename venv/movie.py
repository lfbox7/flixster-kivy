'''
Object model class for Movie
allows full access to the object for future expansion
class also creates specific sub-models for each view
'''

import requests
import json


class Movie(object):
    # constructor
    def __init__(self, id, title, image, backdrop, genre, description, release_date, votes, average):
        self.id = id
        self.title = title
        self.image: str = f"https://image.tmdb.org/t/p/w154/{image}"
        self.backdrop: str = f"https://image.tmdb.org/t/p/w780/{backdrop}"
        self.genre = genre
        self.description = description
        self.release_date = release_date
        self.votes = votes
        self.average = average
    '''
    Getters
    '''
    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_image(self):
        return self.image

    def get_backdrop(self):
        return self.backdrop

    def get_genre(self):
        return self.genre

    def get_description(self):
        return self.description

    def get_release_date(self):
        return self.release_date

    def get_release_votes(self):
        return self.votes

    def get_average(self):
        return self.average

    # class method to create sub-model for main screen recycler view
    @classmethod
    def get_dictionary(cls, movie):
        films = {}
        films['source'] = movie.get_image()
        films['title'] = movie.get_title()
        films['description'] = movie.get_description()
        return films

    # class method to retrieve JSON from themoviedb api's Now Playing option
    # this method will be expanded whn more views are available as the url string can be set as a list variable
    # to allow pulls to retrieve other options such as Most Watched, Highest Rated, by Genre, etc
    @classmethod
    def get_current(cls):
        movie_json = requests.get(
            url="https://api.themoviedb.org/3/movie/now_playing?api_key=ca842d522c78bb859a9e91e0373c4ee3&language=en-US&page=1").json()
        if '__try__':
            movie_dict = movie_json
            del movie_dict['dates']
            del movie_dict['page']
            list_movie_dict = movie_dict['results']
            result = []
            for item in list_movie_dict:
                movie = Movie(item['id'], item['title'], item['poster_path'], item['backdrop_path'], item['genre_ids'],
                              item['overview'], item['release_date'], item['vote_count'], item['vote_average'])
                result.append(movie)
            return result
