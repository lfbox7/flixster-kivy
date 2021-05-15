'''
Main view controller for the movie 'cells' depicted on the recycler view on the main screen
'''

import kivy
from kivy.app import App
from kivy.properties import ListProperty
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
# import the movie model to access api and attributes
from movie import Movie
# import next level up in recycler view hierarchy
from selectable_label import SelectableLabel


class MovieCell(RecycleView):
    # create class variables
    data = ListProperty(allownone=True)
    movie_list = ListProperty([])

    def __init__(self, **kwargs):
        super(MovieCell, self).__init__(**kwargs)
        # call movie model that returns currently playing movie object
        movies = Movie.get_current()
        # for loop to unwrap the object and insert each movie into a dictionary
        for movie in movies:
            self.movie_list.append(Movie.get_dictionary(movie))
        # the most difficult line to create in this application
        # inserts each movie's selected attributes into a 'cell' within the recycler view
        # this code is linked to both SelectableLabel.refresh_view_attrs() and my.kv
        # each of the three labels is the label for each of the three gridlayout segments
        # because this is information is parsed from an object, it is difficult to parse in python
        self.data = [{'label1': {'source': movie['source']}, 'label2': {'text': movie['title']},
                      'label3': {'text': movie['description']}} for movie in self.movie_list]
