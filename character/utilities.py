import sys
# sys.path.append(r'D:\PROGRAMMING\python\bani\Genshin-Impact-OOP-master\New Genshin Impact')

from character.character import Character
from character.hero.hero import hero_list, basic_hero_list
character_list = [
    {
        "name" : "Traveler",
        "role" : 2,
        "hp": 932,
        "armor": 89,
        "type": "basic",
        "basic_attack_damage": 65,
        "exp": 0
    },
    {
        "name" : "Amber",
        "role" : 2,
        "hp": 1187,
        "armor": 70,
        "type": "basic",
        "basic_attack_damage": 51,
        "exp": 0
    },
    {
        "name" : "Lisa",
        "role" : 2,
        "hp": 1054,
        "armor": 78,
        "type": "basic",
        "basic_attack_damage": 57,
        "exp": 0
    },
    {
        "name" : "Kaeya",
        "role" : 2,
        "hp": 1008,
        "armor": 80,
        "type": "basic",
        "basic_attack_damage": 59,
        "exp": 0
    },
]

def generate_character():
    # print("Generating characters")
    for i, character in enumerate(character_list):
        # print(f"character {i+1}: \n{character['name']}")
        new_character = Character(name=character['name'],hp=character['hp'],armor=character['armor'])
        # print(f"character role: {character['role']}")
        # print(f"data type: {type(character['role'])}")
        if character['role'] == 1:
            pass
        elif character['role'] == 2:
            new_character.set_role(character['role'])
            hero_list.append(new_character)
            if character['type'] == 'basic':
                basic_hero_list.append(new_character)
            
    
    # print(f"list of generated hero: {hero_list}")