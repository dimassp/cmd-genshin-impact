import sys, time
import keyboard

from player.player import Player
from utilities import write_per_character, clear_screen
# sys.path.append(r'D:\PROGRAMMING\python\bani\Genshin-Impact-OOP-master\New Genshin Impact')

def start_game(player: Player):
    is_loopable = True
    intro_text = [
        {
            "text": f"Welcome, {player.get_username()}!\n",
            "delay": 0.05,
            "sleeptime": 2,
            "clear_screen": False
        },
        {
            "text": "This is your first time exploring the world of fantasy. Right? ",
            "delay": 0.05,
            "sleeptime": 1.5,
            "clear_screen": False
        },
        {
            "text": "There are so many interesting things you can do here!!!\n\n",
            "delay": 0.05,
            "sleeptime": 2,
            "clear_screen": False
        }    
    ]
    while is_loopable:
        for text in intro_text:
            write_per_character(text['text'],text['delay'])
            if text['clear_screen']:
                clear_screen(text['sleeptime'])
            else:
                time.sleep(text['sleeptime'])
        get_tutorial = ''
        while get_tutorial.lower() != 'y' and get_tutorial.lower() != 'n':
            get_tutorial = input(r"""Do you want to have some tutorials? [Y\N]: """)
            if get_tutorial.lower() != 'y' and get_tutorial.lower() != 'n':
                clear_screen(0)
                print("Sorry, we haven't any option of that\n")
        time.sleep(3)
        
        print(f"You've got some quite interesting heroes to use.")
        for i, hero in enumerate(player.get_hero_owned()):
            print(f"{i+1}. {hero.get_name()}")
        is_loopable = False
        
def continue_game_with_player(player: Player):
    pass