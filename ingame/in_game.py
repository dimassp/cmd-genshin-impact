import sys
import time
import keyboard

from player.player import Player
from ingame.utilities import get_text, iterate_text
from utilities import write_per_character, clear_screen
# sys.path.append(r'D:\PROGRAMMING\python\bani\Genshin-Impact-OOP-master\New Genshin Impact')

class Game():
    def __init__(self, player: Player, game_level: int=1):
        self.player = player
        self.game_level = game_level
        
        pass
    
    def start_game(self):
        clear_screen(0)
        iterate_text('continue_text', self.player, 0, 0)

    
class Tutorial(Game):
    def __init__(self, player: Player, game_level: int = 1):
        self.is_loopable = True
        self.steps_of_tutorial = {
            1: self.tutorial_intro,
            2: self.get_hero_information,
            3: self.end_of_tutorial
        }
        super().__init__(player, game_level)
    
    def start_game(self):
        while self.is_loopable:
            get_tutorial = self.intro_and_get_tutorial()
            
            if get_tutorial.lower() == 'y':
                for i in range(1, len(self.steps_of_tutorial)+1):
                    print(f"current step from outside: {i}")
                    # if i != len(self.steps_of_tutorial) and i !=1: #check if current step is not at the end of the tutorial
                    if i == 1 or i == len(self.steps_of_tutorial):
                        print(f"current step from i equals 1: {i} or current step equals total step")
                        self.steps_of_tutorial[i]()
                    else:
                        print(f"current step: {i}")
                        proceed_or_not = self.proceed_to_next_tutorial_func()
                        if proceed_or_not == 'y': #move to next tutorial if player chose to carry on the tutorial
                            self.steps_of_tutorial[i]()
                        
                        elif proceed_or_not == 'n': #will end the tutorial if the player chose not to continue the tutorial
                            write_per_character("Alright, then.",0.05, 1.5)
                            write_per_character(" Take care when you're in the wild world of this fantasy for I no longer be with you.",0.05,1.5)
                            break
                        
                # self.tutorial_intro()
            else:
                print(f"You chose not to take the tutorial... Enjoy the game!!!")
                time.sleep(2)
            self.is_loopable = False
    def intro_and_get_tutorial(self):
        iterate_text("intro_text", self.player, 0, 0) #Shows player to the texts of introduction to the game 
        get_tutorial = ''
        while get_tutorial.lower() != 'y' and get_tutorial.lower() != 'n':
            write_per_character("""\nDo you want to have some tutorials?""" + r""" [Y/N]""",0.05,0)
            get_tutorial = input(": ")
            if get_tutorial.lower() != 'y' and get_tutorial.lower() != 'n':
                clear_screen(0)
                write_per_character("""Sorry, we haven't any option for that.""",0.05,1)
                print("")
        clear_screen(0)
        return get_tutorial.lower()
        # if get_tutorial.lower() == 'y':
        #     self.tutorial()
        # pass
    def tutorial_intro(self):
        iterate_text("tutorial_intro", self.player, 0, 5) #Shows player to the texts of tutorial of the game 
        for i, hero in enumerate(self.player.get_hero_owned()):
            write_per_character(f"{i+1}. {hero.get_name()}", 0.05, 1)
            # write_per_character(f"", 0, 0)
            print()
        iterate_text("tutorial_intro", self.player, 6,8) #texts of tutorial from index 3 up to index 5
    
    def get_hero_information(self):
        _continue = True
        iterate_text('get_hero_information_text', self.player, 0, 1)
        print()
        heroes_owned = self.player.get_hero_owned()
        while _continue:
            for i, hero in enumerate(heroes_owned):
                write_per_character(f"{i+1}. {hero.get_name()}", 0.05, 0.8)
                print()
            write_per_character("Choose Hero: ",0.05,0)
            try:
                choose_hero = input("")
                choose_hero = int(choose_hero)
                clear_screen(0)
                if choose_hero<1 or choose_hero > len(heroes_owned)+1:
                    write_per_character(f"You only have {len(heroes_owned)} hero(es) by the way...", 0.05, 1.5) 
                    print()   
                else: 
                    print(f"Hero Name: {heroes_owned[choose_hero-1].get_name()}")
                    print(f"Hero Level: {heroes_owned[choose_hero-1].get_level()}")
                    print(f"Hero Basic Attack Damage: {heroes_owned[choose_hero-1].get_basic_attack_damage()}")
                    print(f"Hero Basic Armor: {heroes_owned[choose_hero-1].get_armor()}")
                    print(f"Hero HP: {heroes_owned[choose_hero-1].get_hp()}")
                    print(f"Hero EXP: {heroes_owned[choose_hero-1].get_exp()}")
                    yes_no_question = ''
                    while yes_no_question.lower() != 'n' and yes_no_question.lower() != 'y':
                        write_per_character("Do you want to see the other one? [Y/N]: ", 0.05,0)
                        yes_no_question = input("")
                        if yes_no_question.lower() != 'n' and yes_no_question.lower() != 'y':
                            write_per_character("Sorry,",0.05, 1.5)
                            write_per_character(" your input doesn't seem quite right. Try again", 0.05, 1.5)
                            clear_screen(0)
                    if yes_no_question == 'n':
                        # print("Good bye...")
                        # time.sleep(2)
                        break
                    clear_screen(0)
            except ValueError:
                write_per_character("Sorry,",0.05, 1.5)
                write_per_character(" your input doesn't seem quite right. Try again", 0.05, 1.5)
                clear_screen(0)
    def proceed_to_next_tutorial_func(self):
        proceed_to_next_tutorial_text = f"""\nDo you want to proceed this step? [Y/N]: """
        proceed_to_next_tutorial = ''
        wrong_answer = True
        # Will loop if the player input neither 'y' nor 'n'
        while wrong_answer:
            write_per_character(proceed_to_next_tutorial_text, 0.05, 1)#texts of tutorial from index 3 up to index 5
            proceed_to_next_tutorial = input("")
            clear_screen(0)
            if proceed_to_next_tutorial.lower() != 'y' and proceed_to_next_tutorial.lower() != 'n':
                write_per_character("Sorry. ", 0.05, 1)
                write_per_character("Your answer doesn't seem quite right.", 0.05, 0)
                clear_screen(1)
            else:
                break
        
        return proceed_to_next_tutorial
    
    def end_of_tutorial(self):
        pass
    # def tutorial(self):
    #     self.tutorial_intro()
    #     proceed_or_not = self.proceed_to_next_tutorial_func()
    #     print(f"proceed_to_next_tutorial: {proceed_or_not}")
    #     pass