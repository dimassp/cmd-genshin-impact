import sys
import time
import keyboard

from player.player import Player
from player.utilities import player_input
# from player.utilities import player_input
from maps.maps import maps, maps_2
from maps.utilities import choose_maps
from ingame.utilities import get_text, iterate_text
from utilities import write_per_character, clear_screen, yes_no_question_func ,keyboardDisable
# sys.path.append(r'D:\PROGRAM=MING\python\bani\Genshin-Impact-OOP-master\New Genshin Impact')

from pynput.keyboard import *

class Game():
    def __init__(self, player: Player, game_level: int=1):
        self.player = player
        self.game_level = game_level
        self.map = None
        self.is_loopable = True
        pass
    
    def set_map(self, value: dict):
        self.map = value
    
    def get_map(self):
        return self.map
    
    def start_game(self):
        clear_screen(0)
        iterate_text('continue_text', self.player, 0, 0)
        chosen_maps = choose_maps()
        self.set_map(chosen_maps)
        current_map = self.get_map()
        # print(f"check if exits: {self.player.get_explored_maps().get(current_map)}")
        if self.player.get_explored_maps().get(current_map) is None:
            self.player.set_explored_maps(current_map.get_name(), current_map)
        # print(f"check if exits second: {self.player.get_explored_maps()[current_map.get_name()]}")
        listener = Listener(on_press=lambda event: player_input(event, self.player.get_explored_maps()[current_map.get_name()], self.player, self))
        listener.start()
        while self.is_loopable:
            if not self.is_loopable: 
                listener.stop()
        
        # print("Hello world after while True")
        # time.sleep(5)
    
    # def continue_game(self):
    #     print("Hello world from continue game")

    
class Tutorial(Game):
    def __init__(self, player: Player, game_level: int = 1):
        self.is_loopable = True
        self.steps_of_tutorial = {
            1: self.tutorial_intro,
            2: self.get_hero_information,
            3: self.end_of_tutorial
        }
        super().__init__(player, game_level)
        # self.
    
    def start_game(self):
        while self.is_loopable:
            # disable = keyboardDisable()
            # disable.stop()
            get_tutorial = self.intro_and_get_tutorial()
            if get_tutorial.lower() == 'y':
                for i in range(1, len(self.steps_of_tutorial)+1):
                            
                    if i == 1 or i == len(self.steps_of_tutorial):
                        self.steps_of_tutorial[i]()
                        
                    else:
                        yes_no_question = yes_no_question = yes_no_question_func("\nDo you want to proceed this step? [Y/N]: ")
                        if yes_no_question == 'y': #move to next tutorial if player chose to carry on the tutorial
                            self.steps_of_tutorial[i]()
                        
                        elif yes_no_question == 'n': #will end the tutorial if the player chose not to continue the tutorial
                            write_per_character("Alright, then.",0.03, 1.5)
                            write_per_character(" Take care when you're in the wild world of this fantasy for I no longer be with you.",0.03,1.5)
                            break
                        
            else:
                write_per_character("You chose not to take the tutorial...",0.03,1)
                write_per_character(" Enjoy the game!!!",0.03,1.5)
                print()
                # time.sleep(2)
            self.is_loopable = False
    def intro_and_get_tutorial(self):
        iterate_text("intro_text", self.player, 0, 0) #Shows player to the texts of introduction to the game 
        yes_no_question = yes_no_question_func("Do you want to have some tutorials? [Y/N]: ")
        clear_screen(0)
        return yes_no_question
        
    def tutorial_intro(self):
        iterate_text("tutorial_intro", self.player, 0, 5) #Shows player to the texts of tutorial of the game 
        for i, hero in enumerate(self.player.get_hero_owned()):
            write_per_character(f"{i+1}. {hero.get_name()}", 0.03, 1)
            print()
        iterate_text("tutorial_intro", self.player, 6,8) #texts of tutorial from index 3 up to index 5
    
    def get_hero_information(self):
        _continue = True
        iterate_text('get_hero_information_text', self.player, 0, 1)
        print()
        heroes_owned = self.player.get_hero_owned()
        while _continue:
            for i, hero in enumerate(heroes_owned):
                write_per_character(f"{i+1}. {hero.get_name()}", 0.03, 0.8)
                print()
            write_per_character("Choose Hero: ",0.03,0)
            try:
                choose_hero = input("")
                choose_hero = int(choose_hero)
                clear_screen(0)
                if choose_hero<1 or choose_hero > len(heroes_owned):
                    write_per_character(f"You only have {len(heroes_owned)} hero(es) by the way...", 0.03, 1.5) 
                    print()   
                else: 
                    print(f"Hero Name: {heroes_owned[choose_hero-1].get_name()}")
                    print(f"Hero Level: {heroes_owned[choose_hero-1].get_level()}")
                    print(f"Hero Basic Attack Damage: {heroes_owned[choose_hero-1].get_basic_attack_damage()}")
                    print(f"Hero Basic Armor: {heroes_owned[choose_hero-1].get_armor()}")
                    print(f"Hero HP: {heroes_owned[choose_hero-1].get_hp()}")
                    print(f"Hero EXP: {heroes_owned[choose_hero-1].get_exp()}")
                    yes_no_question = yes_no_question_func("Do you want to see the other one? [Y/N]: ")
                    if yes_no_question == 'n':
                        break
                    clear_screen(0)
            except ValueError:
                write_per_character("Sorry,",0.03, 1.5)
                write_per_character(" your input doesn't seem quite right. Try again", 0.03, 1.5)
                clear_screen(0)
    
    def end_of_tutorial(self):
        pass