import sys
# sys.path.append(r'D:\PROGRAMMING\python\bani\Genshin-Impact-OOP-master\New Genshin Impact')
from character.character import Character

hero_list = list()
starter_hero_list = list()
basic_hero_list = list()

starter_hero_dict = dict()
basic_hero_dict = dict()


class Hero(Character):
    def __init__(self, name: str = "", role: str = "", 
                 type: str = "", current_hp: int = 0,
                 max_hp: int = 0, armor: int = 0, 
                 basic_attack_damage: int = 0, level: int=0,
                 exp: int=0):
        super().__init__(name, role, type, current_hp, max_hp, armor, basic_attack_damage)

        self.__level = level
        self.__exp = exp
    
    #     self.exp_per_level ={
    #         1: 200,
    #         2: 539,
    #         3: 992,
    #         4: 1390,
    #         5: 2122,
    #         6: 4251,
    #         7: 8129,
    #         8: 10923,
    #         9: 12319,
    #         10: 15231
    #     }
    def get_exp(self):
        return self.__exp
    
    def set_exp(self, exp_point: int):
        self.__exp = self.__exp + exp_point
        if self.__exp > 15231:
            self.__exp = 15231
            self.__level = "Max Level"
        if self.__exp < 200:
            self.__level=1
        elif self.__exp >= 200 and self.__exp < 539:
            self.__level=2
        elif self.__exp >= 539 and self.__exp < 992:
            self.__level=3
        elif self.__exp >= 992 and self.__exp < 1390:
            self.__level=4
        elif self.__exp >= 1390 and self.__exp < 2122:
            self.__level=5
        elif self.__exp >= 2122 and self.__exp < 4251:
            self.__level=6
        elif self.__exp >= 4251 and self.__exp < 8129:
            self.__level=7
        elif self.__exp >= 10923 and self.__exp < 12319:
            self.__level=9
        elif self.__exp >= 12319 and self.__exp <= 15231:
            self.__level=10
    
    def set_max_hp(self):
        self.__max_hp = self.__max_hp * self.get_level()
        
    def get_level(self):
        return self.__level
    
    
        
    
        