'''
View controller for inner layout of main screen
'''

from kivy.properties import BooleanProperty
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.recycleview.views import RecycleDataViewBehavior
# import outer layout's view controller class
from selectable_recycle_box_layout import SelectableRecycleBoxLayout

# selectable label class creates a 'selectable' 'cell' within the recycle view
class SelectableLabel(RecycleDataViewBehavior, GridLayout):
    ''' Add selection support to the Label '''
    # index used for cell construction for selectability
    index = None
    # set for none selected but all selectable
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    # set gridlayout to two columns for crisp display within each 'cell'
    cols = 2

    # workhorse function, sets variables for the recycle view 'cells'
    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        # allows for entire dictionary to be selectable in r
        self.index = index
        # property settings for Image on main screen of app
        self.label1_source = data['label1']['source']
        # property setting for Title on main screen of app
        self.label2_text = data['label2']['text']
        # property setting for Description on main screen of app
        self.label3_text = data['label3']['text']
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    # allows for selecting of the 'cell'
    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    # function to do something when the 'cell' is selected
    # currently this function only prints 'cell' information to the console
    # in assignment 4 this will be used to open new screen depicting the movie's entire page
    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))
