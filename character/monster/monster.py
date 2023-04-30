import sys
sys.path.append(r'D:\PROGRAMMING\python\bani\Genshin-Impact-OOP-master\New Genshin Impact')

basic_monster_list = list()
monster_list = list()
from character.character import Character
class Monster(Character):
    def __init__(self, name: str = "", role: str = "", hp: int = 0, armor: int = 0, 
                 basic_attack_damage: int = 0, level: int = 1, exp: int = 0):
        super().__init__(name, role, hp, armor, basic_attack_damage, level, exp)
        
