import sys, time
# sys.path.append(r'D:\PROGRAMMING\python\bani\Genshin-Impact-OOP-master\New Genshin Impact')

from character.character import Character
from character.hero.hero import (Hero, hero_list, 
                                 starter_hero_list, 
                                 basic_hero_list,
                                 starter_hero_dict,
                                 basic_hero_dict)
from character.monster.monster import Monster, monster_list, basic_monster_list, monster_list_2, basic_monster_list_2

from utilities import clear_screen
character_list = [
    
    ##              ##
    ## STARTER HERO ##
    ##              ##
    {
        "name" : "Traveler",
        "role" : 2,
        "max_hp": 932,
        "hp": 932,
        "armor": 89,
        "type": "starter",
        "basic_attack_damage": 65,
        "level": 1,
        "exp": 0
    },
    {
        "name" : "Amber",
        "role" : 2,
        "max_hp": 1187,
        "hp": 1187,
        "armor": 70,
        "type": "starter",
        "basic_attack_damage": 51,
        "level": 1,
        "exp": 0
    },
    {
        "name" : "Lisa",
        "role" : 2,
        "max_hp": 1054,
        "hp": 1054,
        "armor": 78,
        "type": "starter",
        "basic_attack_damage": 57,
        "level": 1,
        "exp": 0
    },
    {
        "name" : "Kaeya",
        "role" : 2,
        "max_hp": 1008,
        "hp": 1008,
        "armor": 80,
        "type": "starter",
        "basic_attack_damage": 59,
        "level": 1,
        "exp": 0
    },
    ##            ##
    ## BASIC HERO ##
    ##            ##
    {
        "name" : "Black Tassel",
        "role" : 2,
        "max_hp": 1200,
        "hp": 1200,
        "armor": 123,
        "type": "basic",
        "basic_attack_damage": 89,
        "level": 1,
        "exp": 0
    },
    {
        "name" : "Sling Shot",
        "role" : 2,
        "max_hp": 1191,
        "hp": 1191,
        "armor": 70,
        "type": "basic",
        "basic_attack_damage": 69,
        "level": 1,
        "exp": 0
    },
    {
        "name" : "Raven Bow",
        "role" : 2,
        "max_hp": 2127,
        "hp": 2127,
        "armor": 52,
        "type": "basic",
        "basic_attack_damage": 67,
        "level": 1,
        "exp": 0
    },
    {
        "name" : "Cool Steel",
        "role" : 2,
        "max_hp": 997,
        "hp": 997,
        "armor": 71,
        "type": "basic",
        "basic_attack_damage": 91,
        "level": 1,
        "exp": 0
    },
    ##                ##
    ## BASIC MONSTERS ##
    ##                ##    
    {
        "name" : "Cyro Slime",
        "role" : 1,
        "max_hp": 112,
        "hp": 112,
        "armor": 8,
        "type": "basic",
        "basic_attack_damage": 11,
        "exp_gained": 80
    },
    {
        "name" : "Dendro Slime",
        "role" : 1,
        "max_hp": 98,
        "hp": 98,
        "armor": 13,
        "type": "basic",
        "basic_attack_damage": 9,
        "exp_gained": 80
    },
    {
        "name" : "Hydro Slime",
        "role" : 1,
        "max_hp": 105,
        "hp": 105,
        "armor": 11,
        "type": "basic",
        "basic_attack_damage": 12,
        "exp_gained": 80
    },
    {
        "name" : "Pyro Slime",
        "role" : 1,
        "max_hp": 205,
        "hp": 205,
        "armor": 15,
        "type": "basic",
        "basic_attack_damage": 19,
        "exp_gained": 80
    },
    {
        "name" : "Electro Slime",
        "role" : 1,
        "max_hp": 155,
        "hp": 155,
        "armor": 19,
        "type": "basic",
        "basic_attack_damage": 14,
        "exp_gained": 80
    },
    {
        "name" : "Geo Slime",
        "role" : 1,
        "max_hp": 165,
        "hp": 165,
        "armor": 16,
        "type": "basic",
        "basic_attack_damage": 17,
        "exp_gained": 80
    },
    {
        "name" : "Anemo Slime",
        "role" : 1,
        "max_hp": 185,
        "hp": 185,
        "armor": 21,
        "type": "basic",
        "basic_attack_damage": 25,
        "exp_gained": 80
    },
]
character_dict = {
    
    ##              ##
    ## STARTER HERO ##
    ##              ##
    "Traveler": {
        "role" : 2,
        "max_hp": 932,
        "hp": 932,
        "armor": 89,
        "type": "starter",
        "basic_attack_damage": 65,
        "level": 1,
        "exp": 0
    },
    "Amber": {
        # "name" : "Amber",
        "role" : 2,
        "max_hp": 1187,
        "hp": 1187,
        "armor": 70,
        "type": "starter",
        "basic_attack_damage": 51,
        "level": 1,
        "exp": 0
    },
    "Lisa": {
        # "name" : "Lisa",
        "role" : 2,
        "max_hp": 1054,
        "hp": 1054,
        "armor": 78,
        "type": "starter",
        "basic_attack_damage": 57,
        "level": 1,
        "exp": 0
    },
    "Kaeya": {
        # "name" : "Kaeya",
        "role" : 2,
        "max_hp": 1008,
        "hp": 1008,
        "armor": 80,
        "type": "starter",
        "basic_attack_damage": 59,
        "level": 1,
        "exp": 0
    },
    ##            ##
    ## BASIC HERO ##
    ##            ##
    "Black Tassel": {
        # "name" : "Black Tassel",
        "role" : 2,
        "max_hp": 1200,
        "hp": 1200,
        "armor": 123,
        "type": "basic",
        "basic_attack_damage": 89,
        "level": 1,
        "exp": 0
    },
    "Sling Shot": {
        # "name" : "Sling Shot",
        "role" : 2,
        "max_hp": 1191,
        "hp": 1191,
        "armor": 70,
        "type": "basic",
        "basic_attack_damage": 69,
        "level": 1,
        "exp": 0
    },
    "Raven Bow": {
        # "name" : "Raven Bow",
        "role" : 2,
        "max_hp": 2127,
        "hp": 2127,
        "armor": 52,
        "type": "basic",
        "basic_attack_damage": 67,
        "level": 1,
        "exp": 0
    },
    "Cool Steel": {
        # "name" : "Cool Steel",
        "role" : 2,
        "max_hp": 997,
        "hp": 997,
        "armor": 71,
        "type": "basic",
        "basic_attack_damage": 91,
        "level": 1,
        "exp": 0
    },
    ##                ##
    ## BASIC MONSTERS ##
    ##                ##    
    "Cyro Slime": {
        # "name" : "Cyro Slime",
        "role" : 1,
        "max_hp": 112,
        "hp": 112,
        "armor": 8,
        "type": "basic",
        "basic_attack_damage": 11,
        "exp_gained": 80
    },
    "Dendro Slime": {
        # "name" : "Dendro Slime",
        "role" : 1,
        "max_hp": 98,
        "hp": 98,
        "armor": 13,
        "type": "basic",
        "basic_attack_damage": 9,
        "exp_gained": 80
    },
    "Hydro Slime": {
        # "name" : "Hydro Slime",
        "role" : 1,
        "max_hp": 105,
        "hp": 105,
        "armor": 11,
        "type": "basic",
        "basic_attack_damage": 12,
        "exp_gained": 80
    },
    "Pyro Slime": {
        # "name" : "Pyro Slime",
        "role" : 1,
        "max_hp": 205,
        "hp": 205,
        "armor": 15,
        "type": "basic",
        "basic_attack_damage": 19,
        "exp_gained": 80
    },
    "Electro Slime": {
        # "name" : "Electro Slime",
        "role" : 1,
        "max_hp": 155,
        "hp": 155,
        "armor": 19,
        "type": "basic",
        "basic_attack_damage": 14,
        "exp_gained": 80
    },
    "Geo Slime": {
        # "name" : "Geo Slime",
        "role" : 1,
        "max_hp": 165,
        "hp": 165,
        "armor": 16,
        "type": "basic",
        "basic_attack_damage": 17,
        "exp_gained": 80
    },
    "Anemo Slime": {
        # "name" : "Anemo Slime",
        "role" : 1,
        "max_hp": 185,
        "hp": 185,
        "armor": 21,
        "type": "basic",
        "basic_attack_damage": 25,
        "exp_gained": 80
    },
}


def add_to_list_based_on_type(character: dict):
    if character['role'] == 1:
        new_monster = Monster(
            name=character["name"], 
            current_hp=character["hp"], 
            type=character["type"],
            role= character["role"],
            armor=character["armor"], 
            basic_attack_damage=character["basic_attack_damage"],
            exp_gained=character["exp_gained"],
            max_hp=character["max_hp"]
        )
        monster_list.append(new_monster)
        monster_list_2.update({new_monster.get_name(): new_monster})
        if character['type'] == 'basic':
            basic_monster_list.append(new_monster)
            basic_monster_list_2.update({new_monster.get_name(): new_monster})
            
    elif character['role'] == 2:
        new_hero = Hero(
            name=character["name"], 
            current_hp=character["hp"],
            type=character["type"],
            role= character["role"],
            armor=character["armor"],
            basic_attack_damage=character["basic_attack_damage"],
            exp=character["exp"],
            max_hp=character["max_hp"]
        )
        hero_list.append(new_hero)
        if character['type'] == 'starter':
            starter_hero_list.append(new_hero)
            starter_hero_dict.update({new_hero.get_name(): {'hero':new_hero}})
            
        elif character['type'] == 'basic':
            basic_hero_list.append(new_hero)
            basic_hero_dict.update({new_hero.get_name(): {'hero':new_hero}})
        
def generate_character():
    for i, character in enumerate(character_list):
        add_to_list_based_on_type(character)