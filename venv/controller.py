'''
Controller module for Kivy application
'''

import kivy
from kivy.app import App
from kivy.lang import Builder

# import view controller
from movie_cell import MovieCell

# load .kv file
kv = Builder.load_file("my.kv")

# main class to run application
class MovieApp(App):
    def build(self):
        return MovieCell()

# command to run app
if __name__ == "__main__":
    MovieApp().run()
