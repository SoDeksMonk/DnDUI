from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from data.front.character_window import CharacterWindow
from data.front.main_window import MainWindow
from data.front.options_window import OptionsWindow
import config
from data.database.container import SqliteWork
from data.database.initTable import create_database
import sqlite3


#Config.set('graphics', 'resizable', '0')
#Config.set('graphics', 'width', '650')
#Config.set('graphics', 'height', '880') 

class ScreenManagement(ScreenManager):
    """_summary_

    Args:
        ScreenManager (_type_): _description_
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MainWindow())
        self.add_widget(OptionsWindow())
        self.add_widget(CharacterWindow())

class DnDUIApp(App):
    
    _connect = sqlite3.Connection
    """the main class of the program

    Args:
        App (_type_): the class from which the application methods are inherited
    """
    def build(self):
        """the main program launch

        Returns:
            _type_: returns the window manager class
        """
        Window.size = (650, 880)
        Window.minimum_width, Window.minimum_height = (600, 800)

        Builder.load_file(f"{config.FRONT_DIR}/main_window.kv")
        Builder.load_file(f"{config.FRONT_DIR}/options_window.kv")
        Builder.load_file(f"{config.FRONT_DIR}/character_window.kv")
        Builder.load_file(f"{config.PROJECT_DIR}/dndui.kv")

        return ScreenManagement()
    def on_start(self):
        create_database()
        SqliteWork.data_path(config.DATABASE_DIR / "DnDUIDB.db")
        self._connect = SqliteWork.open_connection()
        SqliteWork.initialization_fill(self._connect)
            
    def on_request_close(self):
        return 1
    
    def on_stop(self):
        SqliteWork.close_connection(self._connect)
        
    
if __name__ == "__main__":
    DnDUIApp().run()


