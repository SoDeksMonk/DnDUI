from kivy.uix.screenmanager import ScreenManager, Screen


class OptionsWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'OptionsWindow'

    def back_main_window(self):
        self.manager.current = 'MainWindow'
        return 0