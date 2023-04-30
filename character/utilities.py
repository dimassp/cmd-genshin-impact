import sys, time
# sys.path.append(r'D:\PROGRAMMING\python\bani\Genshin-Impact-OOP-master\New Genshin Impact')

from character.character import Character
from character.hero.hero import hero_list, starter_hero_list, basic_hero_list
from character.monster.monster import monster_list, basic_monster_list

from utilities import clear_screen
character_list = [
    
    ##              ##
    ## STARTER HERO ##
    ##              ##
    {
        "name" : "Traveler",
        "role" : 2,
        "hp": 932,
        "armor": 89,
        "type": "starter",
        "basic_attack_damage": 65,
        "exp": 0
    },
    {
        "name" : "Amber",
        "role" : 2,
        "hp": 1187,
        "armor": 70,
        "type": "starter",
        "basic_attack_damage": 51,
        "exp": 0
    },
    {
        "name" : "Lisa",
        "role" : 2,
        "hp": 1054,
        "armor": 78,
        "type": "starter",
        "basic_attack_damage": 57,
        "exp": 0
    },
    {
        "name" : "Kaeya",
        "role" : 2,
        "hp": 1008,
        "armor": 80,
        "type": "starter",
        "basic_attack_damage": 59,
        "exp": 0
    },
    ##            ##
    ## BASIC HERO ##
    ##            ##
    {
        "name" : "Black Tassel",
        "role" : 2,
        "hp": 1200,
        "armor": 123,
        "type": "basic",
        "basic_attack_damage": 89,
        "exp": 0
    },
    {
        "name" : "Sling Shot",
        "role" : 2,
        "hp": 1191,
        "armor": 70,
        "type": "basic",
        "basic_attack_damage": 69,
        "exp": 0
    },
    {
        "name" : "Raven Bow",
        "role" : 2,
        "hp": 2127,
        "armor": 52,
        "type": "basic",
        "basic_attack_damage": 67,
        "exp": 0
    },
    {
        "name" : "Cool Steel",
        "role" : 2,
        "hp": 997,
        "armor": 71,
        "type": "basic",
        "basic_attack_damage": 91,
        "exp": 0
    },
    ##                ##
    ## BASIC MONSTERS ##
    ##                ##    
    {
        "name" : "Cyro Slime",
        "role" : 1,
        "hp": 112,
        "armor": 8,
        "type": "basic",
        "basic_attack_damage": 11,
    },
    {
        "name" : "Dendro Slime",
        "role" : 1,
        "hp": 98,
        "armor": 13,
        "type": "basic",
        "basic_attack_damage": 9,
    },
    {
        "name" : "Hydro Slime",
        "role" : 1,
        "hp": 105,
        "armor": 11,
        "type": "basic",
        "basic_attack_damage": 12,
    },
    {
        "name" : "Pyro Slime",
        "role" : 1,
        "hp": 205,
        "armor": 15,
        "type": "basic",
        "basic_attack_damage": 19,
    },
    {
        "name" : "Electro Slime",
        "role" : 1,
        "hp": 155,
        "armor": 19,
        "type": "basic",
        "basic_attack_damage": 14,
    },
    {
        "name" : "Geo Slime",
        "role" : 1,
        "hp": 165,
        "armor": 16,
        "type": "basic",
        "basic_attack_damage": 17,
    },
    {
        "name" : "Anemo Slime",
        "role" : 1,
        "hp": 185,
        "armor": 21,
        "type": "basic",
        "basic_attack_damage": 25,
    },
]

def add_to_list_based_on_type(character, new_character: Character):
    if character['role'] == 1:
        monster_list.append(new_character)
        if character['type'] == 'basic':
            basic_monster_list.append(new_character)
            
    elif character['role'] == 2:
        hero_list.append(new_character)
        
        if character['type'] == 'starter':
            starter_hero_list.append(new_character)
            
        elif character['type'] == 'basic':
            basic_hero_list.append(new_character)
        
def generate_character():
    for i, character in enumerate(character_list):
        # print(f"character {i+1}: \n{character['name']}")
        new_character = Character(name=character['name'], hp=character['hp'], armor=character['armor'],
                                  basic_attack_damage=character['basic_attack_damage'])
        new_character.set_role(character['role'])
        add_to_list_based_on_type(character, new_character)
        # if character['role'] == 1:
            # monster_list.append(new_character)
            # pass
        # elif character['role'] == 2:
        #     hero_list.append(new_character)
            # if character['type'] == 'starter':
            #     starter_hero_list.append(new_character)
            # pass
            
    
    # print(f"list of generated hero: {hero_list}")