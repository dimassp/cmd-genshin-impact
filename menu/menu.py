import sys

# sys.path.insert(0,r'D:\PROGRAMMING\python\bert_news_type_and_topic_classification\player')
# sys.path.insert(0,r'D:\PROGRAMMING\python\bert_news_type_and_topic_classification\game')

from player.player import  PWD_CONTEXT, player_list
from maps.maps import maps
from character.monster.monster import monster_list, basic_monster_list
# from character.hero.hero import monster_list, basic_monster_list
from player.utilities import (create_new_player, check_if_player_exist)
# from ingame.in_game import start_game, continue_game_with_player
from ingame.in_game import Tutorial, Game
from utilities import clear_screen

class Menu():
    def __init__(self):
        self.menu = {
            1: self.new_game,
            2: self.continue_game,
            # 3: self.show_maps_info,
            # 4: self.show_monsters,
            3: self.exit_game
        }
        self.is_loopable = True
        self.is_player_exist = False
    
    def print_menu(self):
        print("Welcome To Genshin Impact!\nMenu:")
        print("[1] New Game")
        print("[2] Continue Game")
        # print("[3] Show Maps Info")
        # print("[4] Show Monsters")
        print("[3] Exit Game")
    
    def main(self):
        try:
            self.print_menu()
            select_menu = input("Select Menu: ")
            clear_screen(0)
            try:
                self.choose_menu(select_menu)
                # generate_character()
            except ValueError:
                print("Your input seems doesn't quite right. Try Again")
                clear_screen(1)
        except KeyError:
            print("Menu doesn't exist")
            clear_screen()
            
    def choose_menu(self, select_menu):
        self.menu[int(select_menu)]()
    
    def new_game(self):
        new_player = create_new_player()
        tutorial = Tutorial(new_player)
        tutorial.start_game()
        # start_game(new_player)
        pass
    
    def continue_game(self):
        print("Hello world from function continue game")
        username = str(input("Enter username: "))
        password = str(input("Enter password: "))
        self.is_player_exist = False
        player = None
        self.is_player_exist, index = check_if_player_exist(username)
        if self.is_player_exist:
            # print("player found")
            if PWD_CONTEXT.verify(password, player_list[index].get_password()):
                self.is_player_exist = True
                player = player_list[index]
                continue_game = Game(player)
                continue_game.start_game()
                # continue_game_with_player(player)
                clear_screen(0)
            else:
                print("Username or password is incorrect!\n\n")
                clear_screen(1)
            pass
        print(f"self.is_player_exists variable: {self.is_player_exist}")
        
        if not self.is_player_exist:
            print("Username or password is incorrect!\n\n")
            clear_screen(1)
            self.main()
        pass
    
    def show_maps_info(self):
        for i, map in enumerate(maps):
            print(f"{i+1}. Maps name: {map.get_name()}")
            print(f"Size: {map.get_width()}x{map.get_height()}")
            
    def show_monsters(self):
        for i, map in enumerate(basic_monster_list):
            print(f"{i+1}. Monster name: {map.get_name()}")
            # print(f"Size: {map.get_width()}x{map.get_height()}")
    
    def exit_game(self):
        self.is_loopable = False
        print("Hello world from exit game")