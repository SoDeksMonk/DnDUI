from kivy.config import Config
from kivy.uix.screenmanager import Screen
from kivy.logger import Logger
from kivy.core.window import Window
#Config.set("kivy", "window_icon", "fon.jpg")



class MainWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'MainWindow'
        


    def create_character(self):
        self.manager.current = 'CharacterWindow'
        return 0
    
    def setting(self):
        self.manager.current = 'OptionsWindow'
        return 0
    
    def exit(self):
        Window.close()
        return 0
