import sys, time, dis
from random import *
from .player import Player, player_list
from utilities import clear_screen, write_per_character, yes_no_question_func

from character.utilities import character_dict
from character.hero.hero import starter_hero_list
from character.hero.hero import Hero
from character.monster.monster import monster_list_2, Monster

from maps.maps import Maps



from pynput.keyboard import *
# sys.path.append(r'D:\PROGRAMMING\python\bani\Genshin-Impact-OOP-master\New Genshin Impact')

def create_new_player():
    username = str(input("Enter username: "))
    password = str(input("Enter password: "))
    clear_screen(0)
    new_player = Player(username, password)
    is_player_exist_, index = check_if_player_exist(username)
    if is_player_exist_:
        print(f"Player with username {username} already exist at index {index}. Try another username.")
        clear_screen(1)
        return
    for hero in starter_hero_list:
        new_player.add_hero_collection(hero)
    for hero in starter_hero_list:
        new_player.add_hero_collection_by_dict(hero)
    player_list.append(new_player)
    # print(f"list of player: {player_list}")
    # print(f"Player username: {new_player.get_username()}")
    # clear_screen(2)
    return new_player

def check_if_player_exist(username):
    is_player_exist = False
    for i, player in enumerate(player_list):
        if player.get_username() == username:
            is_player_exist = True
            return is_player_exist, i
    return is_player_exist, None


def get_heroes_owned(player: Player):
    for i, hero in enumerate(player.get_hero_owned_by_dict()):
        hero_obj = player.get_hero_owned_by_dict().get(hero)['hero']
        current_hp = hero_obj.get_current_hp()
        max_hp = hero_obj.get_max_hp()
        basic_attack = hero_obj.get_basic_attack_damage()
        write_per_character(f"{i+1}. {hero}\n", 0.03, 0)
        print(f"HP: {current_hp}/{max_hp} Basic Attack: {basic_attack}")

def get_enemy(enemy: str):
    enemy_from_dict = character_dict.get(enemy)
    generated_enemy = Monster(
        
        name=enemy, 
        role=enemy_from_dict['role'], 
        type=enemy_from_dict['type'], 
        current_hp=enemy_from_dict['hp'], 
        max_hp=enemy_from_dict['max_hp'],
        armor=enemy_from_dict['armor'], 
        basic_attack_damage=enemy_from_dict['basic_attack_damage'],
        exp_gained=enemy_from_dict['exp_gained']
    )
    return generated_enemy

def get_enemy_attribute(enemy: Monster):
    enemy_type = enemy.get_type()
    enemy_basic_attack_damage = enemy.get_basic_attack_damage()
    enemy_armor = enemy.get_armor()
    return enemy_type, enemy_basic_attack_damage, enemy_armor

def get_hero_attribute(hero_selected: Hero):
    hero_name = hero_selected.get_name()
    hero_basic_attack_damage = hero_selected.get_basic_attack_damage()
    hero_max_hp = hero_selected.get_max_hp()
    hero_armor = hero_selected.get_armor()
    
    return hero_name, hero_basic_attack_damage, hero_max_hp, hero_armor

def player_input(key, current_map: Maps, player: Player, _self):
    try:
        if key.char == 'p':
            clear_screen(0)
            print('Pause Menu')
            print('[1] Continue Game')
            print('[2] Show Hotkeys')
            # print('[5] Exit Game')
            choose_menu = input("Choose menu: ")
            clear_screen(0)
            if choose_menu == '1':
                pass
            elif choose_menu == '3':
                print(f"Q: Quit Game. M: Show Map Info. P: Pause Game")
            
        if key.char == 'q':
            yes_no_question = yes_no_question_func("Are you sure want to quit? [Y/N]: ")
            if yes_no_question == 'y':
                _self.is_loopable = False
                
        if key.char == 'm':
            print(f"Map info {current_map.get_tiles()['tiles'].get('10x10')}")
            print(f"Current map name: {current_map.get_name()}")
            print(f"Map size: {current_map.get_width()}x{current_map.get_height()}")
            print(f"Locations:")
            for tile in current_map.get_tiles()['tiles']:
                objects_in_location = current_map.get_tiles()['tiles'].get(tile)
                print(f"\t{tile}: {current_map.get_tiles()['tiles'].get(tile)}")
                try:
                    for monster in objects_in_location['monsters']:
                        print(f"Monster: {monster}")
                except:
                    pass
        if key.char == 'o':
            print(f"owned heroes: {player.get_hero_owned_by_dict()}")
            
    except AttributeError:
        pass
    if key == Key.right:
        player.set_player_location_x(1, current_map, key)
        
    if key == Key.left:
        player.set_player_location_x(-1, current_map, key)
            
    if key == Key.up:
        player.set_player_location_y(1, current_map, key)
        
    if key == Key.down:
        player.set_player_location_y(-1, current_map, key)
    # print(f'location: {str(player.get_player_location_x())}x{str(player.get_player_location_y())}')
    location = f'{str(player.get_player_location_x())}x{str(player.get_player_location_y())}'
    objects_in_tiles = current_map.get_tiles()['tiles'].get(location)
    
    if objects_in_tiles is not None:
        key = [k for k, v in objects_in_tiles.items()][0]
        if key == 'monsters':
            if _self.is_loopable:
                clear_screen(0)
                write_per_character(f"There are {len(objects_in_tiles[key])} monsters here...",0.03,1)
                yes_no_question = yes_no_question_func("Do you want fight them? [Y/N]: ")
                if yes_no_question == 'y':
                    # write_per_character(f"Careful!", 0.03,1.3)
                    # write_per_character(f" they're dangerous....", 0.03,1.3)
                    # print(monster_list_2)
                    clear_screen(0)
                    # print(player.get_hero_owned_by_dict())
                    get_heroes_owned(player)
                    total_heroes_owned = len(player.get_hero_owned_by_dict())
                    choose_hero = str(total_heroes_owned+1)
                    while not int(choose_hero) >= 1 or not int(choose_hero) <= total_heroes_owned:
                        write_per_character(f"Choose your hero to fight enemies: ",0.03,1.2)
                        choose_hero = input("")
                        if not int(choose_hero) >= 1 or not int(choose_hero) <= total_heroes_owned:
                            write_per_character(f"You only have {total_heroes_owned} hero(es)",0.03,1.25)
                            clear_screen(0)
                            get_heroes_owned(player)
                    hero_selected = list(player.get_hero_owned_by_dict())[int(choose_hero)-1]
                    hero_selected = player.get_hero_owned_by_dict().get(hero_selected)['hero']
                    hero_name, hero_basic_attack_damage, hero_max_hp, hero_armor = get_hero_attribute(hero_selected)
                    clear_screen(0)
                    for monster in objects_in_tiles['monsters']:
                        chance = {
                            'basic': 85,
                            'boss': 25
                        }
                        generated_enemy = get_enemy(monster)
                        enemy_type, enemy_basic_attack_damage, enemy_armor = get_enemy_attribute(generated_enemy)
                        hit_chance = chance[enemy_type]
                        while generated_enemy.get_current_hp() > 0:
                            random_val = randint(1,100)
                            hero_current_hp = hero_selected.get_current_hp()
                            enemy_current_hp = generated_enemy.get_current_hp()
                            damage_taken_by_enemy = hero_basic_attack_damage-enemy_armor
                            damage_taken_by_hero = enemy_basic_attack_damage-hero_armor
                            print(f"{hero_name}: {hero_current_hp}/{hero_max_hp} {monster}: {enemy_current_hp}/{generated_enemy.get_max_hp()}",end='\r')
                            if random_val <=hit_chance:
                                generated_enemy.set_current_hp(-damage_taken_by_enemy)
                            else: 
                                hero_selected.set_current_hp(-damage_taken_by_hero)
                            time.sleep(1)
                        
                        clear_screen(0)
                    time.sleep(3)
                    
                    
    
    if _self.is_loopable: 
        print(f"x_pos⏳: {str(player.get_player_location_x())}, y_pos: {str(player.get_player_location_y())}",end='\r')
