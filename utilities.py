from os import system, name
import time, sys
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