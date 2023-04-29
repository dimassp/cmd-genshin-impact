import sys
import time
import keyboard

from player.player import Player
from ingame.utilities import get_text, iterate_text
from utilities import write_per_character, clear_screen
# sys.path.append(r'D:\PROGRAMMING\python\bani\Genshin-Impact-OOP-master\New Genshin Impact')


def start_game(player: Player):
    is_loopable = True
    while is_loopable:
        iterate_text("intro_text", player, 0, 0) #Shows player to the texts of introduction to the game 
        get_tutorial = ''
        while get_tutorial.lower() != 'y' and get_tutorial.lower() != 'n':
            get_tutorial = input(": ")
            if get_tutorial.lower() != 'y' and get_tutorial.lower() != 'n':
                clear_screen(0)
                print("Sorry, we haven't any option of that\n")
        clear_screen(0)
        if get_tutorial.lower() == 'y':
            tutorial(player)
        is_loopable = False

def tutorial_intro(player: Player):
    iterate_text("tutorial_text", player, 0, 5) #Shows player to the texts of tutorial of the game 
    for i, hero in enumerate(player.get_hero_owned()):
        write_per_character(f"{i+1}. {hero.get_name()}", 0.05, 1)
        # write_per_character(f"", 0, 0)
        print()
    iterate_text("tutorial_text",player, 6,8) #texts of tutorial from index 3 up to index 5

def proceed_to_next_tutorial_func():
    proceed_to_next_tutorial_text = f"""\nDo you want to proceed this step? [Y//N]: """
    proceed_to_next_tutorial = ''
    wrong_answer = True
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

def tutorial(player: Player):
    tutorial_intro(player)
    proceed_or_not = proceed_to_next_tutorial_func()
    print(f"proceed_to_next_tutorial: {proceed_or_not}")
    time.sleep(4)
    pass


def continue_game_with_player(player: Player):
    write_per_character(get_text("continue_text", player)[0]['text'],
                        get_text("continue_text", player)[0]['delay'])
    pass
