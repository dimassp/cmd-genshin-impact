import sys
# sys.path.append(r'D:\PROGRAMMING\python\bani\Genshin-Impact-OOP-master\New Genshin Impact')
from character.character import Character

hero_list = list()
basic_hero_list = list()

class Hero(Character):
    def __init__(self, name: str = "", role: str = "", hp: int = 0, armor: int = 0):
        super().__init__(name, role, hp, armor)
    