from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen


class CharacterWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'CharacterWindow'

    

    def back_main_window(self):
        self.manager.current = 'MainWindow'
        return 0