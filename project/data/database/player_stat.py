from math import floor
#from kivy.logger import Logger

class Characteristic:
    """the interface for working with the character
    """
    def __init__(self):
        self._lvl = 1
        self._exp_total = 0
        self._exp_need = 300
        self._exp_current = 0
        self._exp_skale = [0,300,900,2700,6500,14000,23000,34000,48000,64000,85000,
                    100000,120000,140000,165000,195000,225000,265000,305000,355000]
        #base stats
        self._strength = 10
        self._dexterity = 10
        self._constitution = 10
        self._intelligence = 10
        self._wisdom = 10
        self._charisma = 10
    
    _lvl = 1
    _exp_total = 0
    _exp_need = 300
    _exp_current = 0
    _exp_skale = [0,300,900,2700,6500,14000,23000,34000,48000,64000,85000,
                100000,120000,140000,165000,195000,225000,265000,305000,355000]
    #base stats
    _strength = 10
    _dexterity = 10
    _constitution = 10
    _intelligence = 10
    _wisdom = 10
    _charisma = 10
    
    @staticmethod
    def clear():
        pass
    #
    
    #lvl
    @classmethod
    def up_lvl(self):
        """character level up
        """
        while self._exp_current >= self._exp_need:
            self._lvl += 1
            self._exp_current = abs(self._exp_need - self._exp_current)
            self._exp_need = self._exp_skale[self._lvl]
        #print("error up_lvl")
    
    @classmethod
    def get_stats(self, *args) -> list:
        """getting a list of characteristics
            accepts one or more characteristics
        Returns:
            list: returns a list of values
        """
        stat = [getattr(self,f"_{let}") for let in args]
        return stat
    
    @classmethod
    def get_stat(self, name_stat: str) -> int:
        """returns one stat

        Args:
            name_stat (str): feature name

        Returns:
            int: stat
        """
        return getattr(self, f"_{name_stat}")
    
    #update stats (setter)
    @classmethod
    def set_stat(self, name_stat: str, value_stat: int) -> None:
        """sets the value of the characteristic

        Args:
            name_stat (str): the name of the stat
            value_stat (int): the value of the stat
        """
        setattr(self, f"_{name_stat}", value_stat)
    
    @classmethod
    def give_exp_current(self, exp: str, value: int) -> None:
        setattr(self, f"_exp_{exp}", self.get_stat(f"exp_{exp}")+value )
        #Logger.exception(f"Warning:{self.give_exp_current.__name__} in {self} input error")

    
    

    @classmethod
    def up_down_stats(self, name_stat: str, value_stat: int) -> None:
        """changing characteristics
            
        Args:
            name_stat (str): the name of the stat
            value_stat (int): the value of the stat
        """
        setattr(self, f"_{name_stat}", self.get_stat(name_stat)+value_stat )
    
    #update modifier 
    @classmethod
    def get_modifier(self, *args: str) -> list:
        """getting character modifiers
            accepts one or more characteristics
        Returns:
            list: list of modifiers
        """
        new_list = [floor((int(self.get_stat(let)) - 10)/2) for let in args]   
        return new_list


