from kivy.uix.screenmanager import Screen
from kivy.logger import Logger
from Lib.player_stat import Characteristic as Chart
from kivy.event import EventDispatcher


class CharacterWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'CharacterWindow'

        self.ids.lvl_btn.text = Chart.get_lvl(Chart)
        self.ids.exp_cur_nee.text = (Chart.get_exp(Chart, "current")
                                      + "/" + 
                                      Chart.get_exp(Chart, "need"))
        self.ids.str.text = Chart.get_stats(Chart, "strength")
        self.ids.dex.text = Chart.get_stats(Chart, "dexterity")
        self.ids.con.text = Chart.get_stats(Chart, "constitution")
        self.ids.int.text = Chart.get_stats(Chart, "intelligence")
        self.ids.wis.text = Chart.get_stats(Chart, "wisdom")
        self.ids.cha.text = Chart.get_stats(Chart, "charisma")

        self.ids.str_mod.text = Chart.get_modifier(Chart, "strength")
        self.ids.dex_mod.text = Chart.get_modifier(Chart, "dexterity")
        self.ids.con_mod.text = Chart.get_modifier(Chart, "constitution")
        self.ids.int_mod.text = Chart.get_modifier(Chart, "intelligence")
        self.ids.wis_mod.text = Chart.get_modifier(Chart, "wisdom")
        self.ids.cha_mod.text = Chart.get_modifier(Chart, "charisma")

    def reboot(self):
        
        self.ids.lvl_btn.text = Chart.get_lvl(Chart)
        self.ids.exp_cur_nee.text = (Chart.get_exp(Chart, "current")
                                      + "/" + 
                                      Chart.get_exp(Chart, "need"))

        self.ids.str.text = Chart.get_stats(Chart, "strength")
        self.ids.dex.text = Chart.get_stats(Chart, "dexterity")
        self.ids.con.text = Chart.get_stats(Chart, "constitution")
        self.ids.int.text = Chart.get_stats(Chart, "intelligence")
        self.ids.wis.text = Chart.get_stats(Chart, "wisdom")
        self.ids.cha.text = Chart.get_stats(Chart, "charisma")

        self.ids.str_mod.text = Chart.get_modifier(Chart, "strength")
        self.ids.dex_mod.text = Chart.get_modifier(Chart, "dexterity")
        self.ids.con_mod.text = Chart.get_modifier(Chart, "constitution")
        self.ids.int_mod.text = Chart.get_modifier(Chart, "intelligence")
        self.ids.wis_mod.text = Chart.get_modifier(Chart, "wisdom")
        self.ids.cha_mod.text = Chart.get_modifier(Chart, "charisma")
        Chart.up_lvl(Chart)

    def give_exp(self):
        try:
            if self.ids.exp_set.text.isdigit():
                if self.ids.exp_set.focus == False and self.ids.exp_set.text != "":
                    Chart.give_exp_current(Chart, self.ids.exp_set.text)
                    self.ids.exp_set.text = ""
                    Chart.up_lvl(Chart)
            else:
                self.ids.exp_set.text = ""
        except:
            Logger.exception(f"{self.give_exp.__name__} in {self.name} input error")

    def up_char(self, id):
        match id:
            case self.ids.str_up_btn:
                Chart.up_down_stats(Chart, "strength", 1)
            case self.ids.dex_up_btn:
                Chart.up_down_stats(Chart, "dexterity", 1)
            case self.ids.con_up_btn:
                Chart.up_down_stats(Chart, "constitution", 1)
            case self.ids.int_up_btn:
                Chart.up_down_stats(Chart, "intelligence", 1)
            case self.ids.wis_up_btn:
                Chart.up_down_stats(Chart, "wisdom", 1)
            case self.ids.cha_up_btn:
                Chart.up_down_stats(Chart, "charisma", 1)
            case _:
                print("Error up_char")

    def down_char(self, id):
        match id:
            case self.ids.str_down_btn:
                Chart.up_down_stats(Chart, "strength", -1)
            case self.ids.dex_down_btn:
                Chart.up_down_stats(Chart, "dexterity", -1)
            case self.ids.con_down_btn:
                Chart.up_down_stats(Chart, "constitution", -1)
            case self.ids.int_down_btn:
                Chart.up_down_stats(Chart, "intelligence", -1)
            case self.ids.wis_down_btn:
                Chart.up_down_stats(Chart, "wisdom", -1)
            case self.ids.cha_down_btn:
                Chart.up_down_stats(Chart, "charisma", -1)
            case _:
                print("Error down_char")
    
        


    def back_main_window(self):
        Chart.clear(Chart)
        self.reboot()
        self.manager.current = 'MainWindow'
        return 0