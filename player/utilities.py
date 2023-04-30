import sys, time
from .player import Player, player_list
from utilities import clear_screen
from character.hero.hero import starter_hero_list
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
