import sys
sys.path.append(r'D:\PROGRAMMING\python\bani\Genshin-Impact-OOP-master\New Genshin Impact')

basic_monster_list = list()
basic_monster_list_2 = dict()
monster_list = list()
monster_list_2 = dict()
from character.character import Character
class Monster(Character):
    def __init__(self, name: str = "", role: str = "", 
                 type: str = "", current_hp: int = 0, 
                 max_hp: int = 0, armor: int = 0, 
                 basic_attack_damage: int = 0, exp_gained: int=0):
        super().__init__(name, role, type, current_hp, max_hp, armor, basic_attack_damage)
        self.__exp_gained = exp_gained
        
    def get_exp_gained(self):
        return self.__exp_gained
    
    def set_exp_gained(self, value: int):
        self.__exp_gained = self.__exp_gained * value
        
