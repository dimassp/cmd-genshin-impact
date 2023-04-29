import time

from player.player import Player
from utilities import write_per_character, clear_screen

def iterate_text(text_type: str, player: Player, start: int, end: int):
    # time.sleep(4)
    texts = ""
    if end == 0:
        texts = get_text(text_type, player)[start:]
    if start == 0:
        texts = get_text(text_type, player)[:end+1]
    if start == 0 and end == 0:
        texts = get_text(text_type, player)
    if start != 0 and end !=0:
        texts = get_text(text_type, player)[start:end+1]
    # print(f"texts: {texts}")
    # time.sleep(5)
    for text in texts:
        write_per_character(text['text'], text['delay'], text['sleeptime'])
        if text['clear_screen']:
            clear_screen(0)
        # else:
        #     time.sleep(text['sleeptime'])
        
def get_text(text: str, player: Player):
    story_texts = {
        "intro_text" : [
            {
                "text": f"Welcome, {player.get_username()}!\n",
                "delay": 0.05,
                "sleeptime": 2,
                "clear_screen": False
            },
            {
                "text": "This is your first time exploring the world of fantasy. Right?",
                "delay": 0.05,
                "sleeptime": 1.5,
                "clear_screen": False
            },
            {
                "text": " There are so many interesting things you can do here!!!",
                "delay": 0.05,
                "sleeptime": 2,
                "clear_screen": False
            },
            {
                "text": """\n\nDo you want to have some tutorials?""" + r""" [Y\N]""",
                "delay": 0.05,
                "sleeptime": 0,
                "clear_screen": False
            },
        ],
        "tutorial_text": [
            { #0
                "text": f"Great!!!",
                "delay": 0.05,
                "sleeptime": 2,
                "clear_screen": True
            },
            { #1
                "text": f"At the beginning of this game,",
                "delay": 0.05,
                "sleeptime": 1,
                "clear_screen": False
            },
            { #2
                "text": f" You'll have some basic heroes.\n",
                "delay": 0.05,
                "sleeptime": 1,
                "clear_screen": False
            },
            { #3
                "text": f"""You're currently got some quite interesting heroes to utilize,""",
                "delay": 0.05,
                "sleeptime": 1,
                "clear_screen": False
            },
            { #4
                "text": f""" there are {len(player.get_hero_owned())} of them with different exciting skills.""",
                "delay": 0.05,
                "sleeptime": 1,
                "clear_screen": False
            },
            { #5
                "text": " They are: \n",
                "delay": 0.05,
                "sleeptime": 1,
                "clear_screen": False
            },
            { #6
                "text": rf"You can choose any of these heroes as you want so long as you have those heroes.",
                "delay": 0.05,
                "sleeptime": 1.5,
                "clear_screen": False
            },
            { #7
                "text": rf""" In this step of this tutorial,""",
                "delay": 0.05,
                "sleeptime": 1.5,
                "clear_screen": False
            },
            { #8
                "text": rf""" you can either pick one of them to find out their own  informations of the hero you choose or you can skip this step.""",
                "delay": 0.05,
                "sleeptime": 1.5,
                "clear_screen": False
            },
            { #9
                "text": f"""\nDo you want to proceed this step? [Y//N]: """,
                "delay": 0.05,
                "sleeptime": 1.5,
                "clear_screen": False
            },
            # {
            #     "text": rf"You can choose any hero you want so long as you have those heroes.",
            #     "delay": 0.05,
            #     "sleeptime": 1.5,
            #     "clear_screen": False
            # },
        ],
        "continue_text": [
            {
                "text": f"Welcome back to the world of fantasy, {player.get_username()}!",
                "delay": 0.05,
                "sleeptime": 2,
                "clear_screen": False
            }
        ]
    }
    return story_texts[text]