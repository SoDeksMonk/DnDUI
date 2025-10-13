import sys
import os
from kivy.app import App
from kivy.config import Config
from kivymd.app import MDApp
from kivy.graphics.texture import Texture
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Front.character_window import CharacterWindow
from Front.main_window import MainWindow
from Front.options_window import OptionsWindow
#character_window_app = CharacterWindow()
#main_window_app = Window()

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '650')
Config.set('graphics', 'height', '880')
Window.size = (650, 880)
Window.minimum_width, Window.minimum_height = (600, 800)

class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MainWindow())
        self.add_widget(OptionsWindow())
        self.add_widget(CharacterWindow())

class DnDUIApp(App):
    def build(self):
        texture = Texture.create()
        
        


        return ScreenManagement()
    
if __name__ == "__main__":
    DnDUIApp().run()


