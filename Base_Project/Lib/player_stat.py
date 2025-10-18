from math import floor
from kivy.logger import Logger

class Characteristic:
    def __init__(self):
        pass
    def clear(self):
        self.__lvl = 1
        self.__exp_need = 300
        self.__exp_current = 0
        self.__exp_skale = [0,300,900,2700,6500,14000,23000,34000,48000,64000,85000,
                    100000,120000,140000,165000,195000,225000,265000,305000,355000]
        #base stats
        self.__strength = 10
        self.__dexterity = 10
        self.__constitution = 10
        self.__intelligence = 10
        self.__wisdom = 10
        self.__charisma = 10
        #base modifier
        self.__strength_modifier = 0
        self.__dexterity_modifier = 0
        self.__constitution_modifier = 0
        self.__intelligence_modifier = 0
        self.__wisdom_modifier = 0
        self.__charisma_modifier = 0
    #
    __lvl = 1
    __exp_need = 300
    __exp_current = 0
    __exp_skale = [0,300,900,2700,6500,14000,23000,34000,48000,64000,85000,
                   100000,120000,140000,165000,195000,225000,265000,305000,355000]
    #base stats
    __strength = 10
    __dexterity = 10
    __constitution = 10
    __intelligence = 10
    __wisdom = 10
    __charisma = 10
    #base modifier
    __strength_modifier = 0
    __dexterity_modifier = 0
    __constitution_modifier = 0
    __intelligence_modifier = 0
    __wisdom_modifier = 0
    __charisma_modifier = 0

    #lvl
    def up_lvl(self):
        try:
            while self.__exp_current >= self.__exp_need:
                self.__lvl += 1
                self.__exp_current = abs(self.__exp_need - self.__exp_current)
                self.__exp_need = self.__exp_skale[self.__lvl]
        except:
            print("error up_lvl")
    
    def get_lvl(self):
        try:
            return str(self.__lvl)
        except:
            print("error get_lvl")
    
    def get_exp(self, currentOrNeed):
        match currentOrNeed:
            case "current":
                return str(self.__exp_current)
            case "need":
                return str(self.__exp_need)
            case _:
                Logger.exception(f"Warning:{self.get_exp.__name__} in {self} input error")
    
    def give_exp_current(self, value):
        try:
            self.__exp_current += int(value)
        except:
            Logger.exception(f"Warning:{self.give_exp_current.__name__} in {self} input error")

    #update stats (setter)
    def re_stats(self, name_stat, value_stat = 10):
        match name_stat:
            case "strength":
                self.__strength = value_stat
            case "dexterity":
                self.__dexterity = value_stat
            case "constitution":
                self.__constitution = value_stat
            case "intelligence":
                self.__intelligence = value_stat
            case "wisdom":
                self.__wisdom = value_stat
            case "charisma":
                self.__charisma = value_stat
            case _: print("error re_stats")

    def up_down_stats(self, name_stat, value_stat):
        match name_stat:
            case "strength":
                self.__strength += value_stat
            case "dexterity":
                self.__dexterity += value_stat
            case "constitution":
                self.__constitution += value_stat
            case "intelligence":
                self.__intelligence += value_stat
            case "wisdom":
                self.__wisdom += value_stat
            case "charisma":
                self.__charisma += value_stat
            case _: print("error up_down_stats")
    
    #get stats (getter)
    def get_stats(self, name_stat):
        match name_stat:
            case "strength":
                return  str(self.__strength)
            case "dexterity":
                return  str(self.__dexterity)
            case "constitution":
                return  str(self.__constitution)
            case "intelligence":
                return  str(self.__intelligence)
            case "wisdom":
                return  str(self.__wisdom)
            case "charisma":
                return  str(self.__charisma)
            case _: print("error get_stats")

    #update modifier 
    def re_modifier(self):
        try:
            self.__strength_modifier = floor((self.__strength - 10)/2)
            self.__dexterity_modifier = floor((self.__dexterity - 10)/2)
            self.__constitution_modifier = floor((self.__constitution - 10)/2)
            self.__intelligence_modifier = floor((self.__intelligence - 10)/2)
            self.__wisdom_modifier = floor((self.__wisdom - 10)/2)
            self.__charisma_modifier = floor((self.__charisma - 10)/2)
        except:
            print("error re_modifier")


    #get modifier
    def get_modifier(self, name_mod):
        self.re_modifier(self)
        match name_mod:
            case "strength":
                return  str(self.__strength_modifier)
            case "dexterity":
                return  str(self.__dexterity_modifier)
            case "constitution":
                return  str(self.__constitution_modifier)
            case "intelligence":
                return  str(self.__intelligence_modifier)
            case "wisdom":
                return  str(self.__wisdom_modifier)
            case "charisma":
                return  str(self.__charisma_modifier)
            case _: print("error get_stats")
    
    

