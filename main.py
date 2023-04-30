import time
from character.hero.hero import Hero, starter_hero_list, basic_hero_list, hero_list
from menu.menu import Menu
from character.utilities import generate_character
from maps.utilities import generate_maps
def generate_objects():
    generate_character()
    generate_maps()
    # print(f"starter hero total: {len(starter_hero_list)}")
    # print(f"basic hero total: {len(basic_hero_list)}")
    # print(f"total hero: {len(basic_hero_list)}")
    # time.sleep(3)

if __name__ == "__main__":
    generate_objects()
    menu = Menu()
    while menu.is_loopable:
        menu.main()
        pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



                    ###################    
                        
                        
                        
                    ### Unused Code ###



                    ###################


# def main():
#     try:
#         print("Welcome To Genshin Impact!\nMenu:")
#         print("[1] New Game")
#         print("[2] Continue Game")
#         print("[3] Exit Game")
#         select_menu = input("Select Menu: ")
#         menu = Menu(select_menu)
#         try:
#             menu.choose_menu()
#         except ValueError:
#             print("Your input seems doesn't quite right. Try Again")
#     except KeyError:
#         print("Menu doesn't exist")

# player_list = list()
# player1 = Player("dimassuryap", "secret")
# player2 = Player("dimassamid", "secret2")
# player_list.append(player1)
# player_list.append(player2)
# print(player_list)
# for player in player_list:
#     print(player.get_username())    