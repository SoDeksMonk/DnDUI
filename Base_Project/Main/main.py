import sys
import os
from kivy.logger import Logger
from kivy.app import App
from kivy.config import Config
#from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager#, Screen
from kivy.core.window import Window
from kivy.lang import Builder
#from kivy.properties import 

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Front.character_window import CharacterWindow
from Front.main_window import MainWindow
from Front.options_window import OptionsWindow
#from Lib.container import


#Config.set('graphics', 'resizable', '0')
#Config.set('graphics', 'width', '650')
#Config.set('graphics', 'height', '880')


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MainWindow())
        self.add_widget(OptionsWindow())
        self.add_widget(CharacterWindow())

class DnDUIApp(App):
    def build(self):
        Window.size = (650, 880)
        Window.minimum_width, Window.minimum_height = (600, 800)
        
        Builder.load_file("Base_Project/Front/main_window.kv")
        Builder.load_file("Base_Project/Front/options_window.kv")
        Builder.load_file("Base_Project/Front/character_window.kv")
        Builder.load_file("Base_Project/Main/dndui.kv")
        
        


        return ScreenManagement()
    
if __name__ == "__main__":
    DnDUIApp().run()


