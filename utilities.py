from os import system, name
import time, sys
class keyboardDisable():

    def start(self):
        self.on = True

    def stop(self):
        self.on = False

    def __call__(self): 
        while self.on:
            msvcrt.getwch()


    def __init__(self):
        self.on = False
        import msvcrt

# disable = keyboardDisable()
# disable.start()
# time.sleep(10)
# disable.stop()

def clear_screen(sleeptime):
    if name == 'nt':
        time.sleep(sleeptime)
        _ = system('cls')
    else:
        time.sleep(sleeptime)
        _ = system('clear')

def write_per_character(text: str, delay: float, sleeptime: float):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(sleeptime)
    
def yes_no_question_func(text: str):
    yes_no_question = ""
    while yes_no_question.lower() != 'n' and yes_no_question.lower() != 'y':
        write_per_character(text, 0.03,0)
        yes_no_question = input("")
        if yes_no_question.lower() != 'n' and yes_no_question.lower() != 'y':
            write_per_character("Sorry,",0.03, 1.5)
            write_per_character(" your input doesn't seem quite right. Try again", 0.03, 1.5)
            clear_screen(0)
    return yes_no_question.lower()