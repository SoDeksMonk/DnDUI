from kivy.uix.screenmanager import Screen
#from kivy.logger import Logger
from data.database.player_stat import Characteristic as Chart
#from kivy.event import EventDispatcher



class CharacterWindow(Screen):
    _list_stat = [
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
    ]
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'CharacterWindow'

        self.ids.lvl_btn.text = str(Chart.get_stat("lvl"))
        self.ids.exp_cur_nee.text = (str(Chart.get_stat("exp_current"))
                                      + "/" + 
                                      str(Chart.get_stat("exp_need")))

        for let in self._list_stat:
            self.ids.get(let[:3]).text = str(Chart.get_stat(let))

        for let in self._list_stat:
            self.ids.get(f"{let[:3]}_mod").text = str(*Chart.get_modifier(let))
    #updating the data    
    def reboot(self) -> None:
        """updating the data
        """
        self.ids.lvl_btn.text = str(Chart.get_stat("lvl"))
        self.ids.exp_cur_nee.text = (str(Chart.get_stat("exp_current"))
                                      + "/" + 
                                      str(Chart.get_stat("exp_need")))

        for let in self._list_stat:
            self.ids.get(let[:3]).text = str(Chart.get_stat(let))
            
        for let in self._list_stat:
            self.ids.get(f"{let[:3]}_mod").text = str(*Chart.get_modifier(let))
        Chart.up_lvl()

    def give_exp(self) -> None:
        """Transferring experience to a character's class
        """
        if self.ids.exp_set.text.isdigit():
            if not self.ids.exp_set.focus and self.ids.exp_set.text != "":
                Chart.give_exp_current("current", int(self.ids.exp_set.text))
                self.ids.exp_set.text = ""
                Chart.up_lvl()
        else:
            self.ids.exp_set.text = ""
    
    def up_char(self, id):
        match id:
            case self.ids.str_up_btn:
                Chart.up_down_stats("strength", 1)
            case self.ids.dex_up_btn:
                Chart.up_down_stats("dexterity", 1)
            case self.ids.con_up_btn:
                Chart.up_down_stats("constitution", 1)
            case self.ids.int_up_btn:
                Chart.up_down_stats("intelligence", 1)
            case self.ids.wis_up_btn:
                Chart.up_down_stats("wisdom", 1)
            case self.ids.cha_up_btn:
                Chart.up_down_stats("charisma", 1)
            case _:
                print("Error up_char")

    
    def down_char(self, id):
        match id:
            case self.ids.str_down_btn:
                Chart.up_down_stats("strength", -1)
            case self.ids.dex_down_btn:
                Chart.up_down_stats("dexterity", -1)
            case self.ids.con_down_btn:
                Chart.up_down_stats("constitution", -1)
            case self.ids.int_down_btn:
                Chart.up_down_stats("intelligence", -1)
            case self.ids.wis_down_btn:
                Chart.up_down_stats("wisdom", -1)
            case self.ids.cha_down_btn:
                Chart.up_down_stats("charisma", -1)
            case _:
                print("Error down_char")
    
        
    def back_main_window(self):
        #Chart.clear(Chart)
        self.reboot()
        self.manager.current = 'MainWindow'
        return 0