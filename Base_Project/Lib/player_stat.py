from math import floor

class characteristic:
    def __init__(self):
        pass

    #base stats
    __strength = 10
    __dexterity = 10
    __constitution = 10
    __inteligence = 10
    __wisdom = 10
    __charisma = 10
    #base modifier
    __strength_modifier = 0
    __dexterity_modifier = 0
    __constitution_modifier = 0
    __inteligence_modifier = 0
    __wisdom_modifier = 0
    __charisma_modifier = 0

    #update stats (setter)
    def re_stats(self, name_stat, value_stat = 10):
        match name_stat:
            case "strength":
                self.__strength = value_stat
            case "dexterity":
                self.__dexterity = value_stat
            case "constitution":
                self.__constitution = value_stat
            case "inteligence":
                self.__inteligence = value_stat
            case "wisdom":
                self.__wisdom = value_stat
            case "charisma":
                self.__charisma = value_stat
            case _: print("error")
    
    #update modifier 
    def re_modifier(self):
        self.__strength_modifier = floor((self.__strength - 10)/2)
        self.__dexterity_modifier = floor((self.__dexterity - 10)/2)
        self.__constitution_modifier = floor((self.__constitution - 10)/2)
        self.__inteligence_modifier = floor((self.__inteligence - 10)/2)
        self.__wisdom_modifier = floor((self.__wisdom - 10)/2)
        self.__charisma_modifier = floor((self.__charisma - 10)/2)

    #get stats (getter)
    def get_stats(self, name_stat):
        match name_stat:
            case "strength":
                return  self.__strength
            case "dexterity":
                return  self.__dexterity
            case "constitution":
                return  self.__constitution
            case "inteligence":
                return  self.__inteligence
            case "wisdom":
                return  self.__wisdom
            case "charisma":
                return  self.__charisma
            case _: print("error")

