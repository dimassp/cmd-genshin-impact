import sys

# sys.path.insert(0,r'D:\PROGRAMMING\python\bert_news_type_and_topic_classification\player')
# sys.path.insert(0,r'D:\PROGRAMMING\python\bert_news_type_and_topic_classification\game')

from player.player import  PWD_CONTEXT, player_list
from player.utilities import (create_new_player, check_if_player_exist)
from ingame.in_game import start_game, continue_game_with_player
from utilities import clear_screen

class Menu():
    def __init__(self):
        self.menu = {
            1: self.new_game,
            2: self.continue_game,
            3: self.exit_game
        }
        self.is_loopable = True
        self.is_player_exist = False
    
    def main(self):
        try:
            print("Welcome To Genshin Impact!\nMenu:")
            print("[1] New Game")
            print("[2] Continue Game")
            print("[3] Exit Game")
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
        start_game(new_player)
        pass
    
    def continue_game(self):
        print("Hello world from function continue game")
        username = str(input("Enter username: "))
        password = str(input("Enter password: "))
        self.is_player_exist = False
        continue_with_player = None
        self.is_player_exist, index = check_if_player_exist(username)
        if self.is_player_exist:
            # print("player found")
            if PWD_CONTEXT.verify(password, player_list[index].get_password()):
                self.is_player_exist = True
                continue_with_player = player_list[index]
                continue_game_with_player(continue_with_player)
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
    
    def exit_game(self):
        self.is_loopable = False
        print("Hello world from exit game")