import sys
# sys.path.append(r'D:\PROGRAMMING\python\bani\Genshin-Impact-OOP-master\New Genshin Impact')
from character.character import Character

hero_list = list()
starter_hero_list = list()
basic_hero_list = list()
class Hero(Character):
    def __init__(self, name: str = "", role: str = "", hp: int = 0, armor: int = 0, basic_attack_damage: int = 0, level: int = 1, exp: int = 0):
        super().__init__(name, role, hp, armor, basic_attack_damage, level, exp)
        
        self.exp_per_level ={
            1: 200,
            2: 539,
            3: 992,
            4: 1390,
            5: 2122,
            6: 4251,
            7: 8129,
            8: 10923,
            9: 12319,
            10: 15231
        }
    def set_exp(self, value: int):
        self.__exp = self.__exp + value
        
        if self.__exp >= self.exp_per_level[self.get_level()]:
            self.set_level(1)
    