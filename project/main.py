from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from data.front.character_window import CharacterWindow
from data.front.main_window import MainWindow
from data.front.options_window import OptionsWindow
import config
#from data.database.container import SqliteWork


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
    """_summary_

    Args:
        App (_type_): _description_
    """
    def build(self):
        Window.size = (650, 880)
        Window.minimum_width, Window.minimum_height = (600, 800)
        
        #SqliteWork(SqliteWork, 'Base_Project/Lib/character.db')
        #connect = SqliteWork.open_connection(SqliteWork)
        #SqliteWork.initialization_tables(SqliteWork, connect)
        #SqliteWork.close_connection(connect)

        Builder.load_file(f"{config.FRONT_DIR}/main_window.kv")
        Builder.load_file(f"{config.FRONT_DIR}/options_window.kv")
        Builder.load_file(f"{config.FRONT_DIR}/character_window.kv")
        Builder.load_file(f"{config.PROJECT_DIR}/dndui.kv")
        
        


        return ScreenManagement()
    
if __name__ == "__main__":
    DnDUIApp().run()


