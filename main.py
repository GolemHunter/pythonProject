# Kivy imported code to make the app work (it is necessary)
from kivy.uix.image import Image
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
# These classes define all the imports and their parented variables
# this class is for the main window
class MainWindow(Screen):
    pass
# this class is for showing all the months and the return buttons
class EveWindow(Screen):
    pass
# these classes are for the months and their functions in the .kv file
class august(Screen):
    pass
class september(Screen):
    pass
class october(Screen):
    pass
class november(Screen):
    pass
class december(Screen):
    pass
class january(Screen):
    pass
class february(Screen):
    pass
class march(Screen):
    pass
class april(Screen):
    pass
class may(Screen):
    pass
class june(Screen):
    pass
class july(Screen):
    pass
# this is what controls the screens/windows that slide
class WindowManager(ScreenManager):
    pass
# this loads the .kv file
kv = Builder.load_file('screens.kv')
# this is the code that runs the app (required for all apps and can be modified)
class EventsApp(App):
    def build(self):
        return kv
# this is for zeus's group only! do not copy or else we will report to ms Shajia
# Verification to run the app
if __name__ == '__main__':
    EventsApp().run()