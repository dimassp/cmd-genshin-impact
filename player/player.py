import sys
# try:
#     import msvcrt
# except ImportError:
#     import sys, termios
from passlib.context import CryptContext
from character.hero.hero import Hero
from pynput.keyboard import *

# import maps.maps
# sys.path.append(r'D:\PROGRAMMING\python\bani\Genshin-Impact-OOP-master\New Genshin Impact')



PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

player_list = list()
player_list_2 = dict()

class Player():
    def __init__(self, username: str, password: str, ):
        self.__username = username
        self.__password = PWD_CONTEXT.hash(password)
        self.__hero_owned = list()
        self.__hero_owned_by_dict = dict()
        self.__player_location_x: int =0
        self.__player_location_y: int =0
        self.__explored_maps= {}
        
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def get_hero_owned(self):
        return self.__hero_owned
    
    def get_hero_owned_by_dict(self):
        return self.__hero_owned_by_dict
    
    def get_player_location_x(self):
        return self.__player_location_x
    
    def get_player_location_y(self):
        return self.__player_location_y
    def get_explored_maps(self):
        return self.__explored_maps
    def set_explored_maps(self, name: str, map):
        self.__explored_maps.update({name: map})
    def set_player_location_x(self, value: int, current_map, key):
        # print(f"value: {value}")
        # print(f"current_map: {current_map.get_width()}")
        # print(f"key pressed: {key}")
        # print(f"self.get_player_location_x(): {self.get_player_location_x()}")
        if key == Key.right:
            if self.get_player_location_x() + value >= current_map.get_width():
                self.__player_location_x = current_map.get_width()
            else:
                self.__player_location_x = self.__player_location_x + value
            
        if key == Key.left:
            if self.get_player_location_x() + value <= 0:
                # print("self.get_player_location_x() + value <= 0")
                self.__player_location_x = 0
            else:
                self.__player_location_x = self.__player_location_x + value
                
        # if self.get_player_location_x()
    
    def set_player_location_y(self, value: int, current_map, key):
        if key == Key.up:
            if self.get_player_location_y() + value >= current_map.get_height():
                self.__player_location_y = current_map.get_height()
            else:
                self.__player_location_y = self.__player_location_y + value
                
        if key == Key.down:
            if self.get_player_location_y() + value <= 0:
                self.__player_location_y = 0
            else:
                self.__player_location_y = self.__player_location_y + value
        
    # def set_player_location_x_2(self, value: int, current_map_width: int):
    #     self.__player_location_x = self.__player_location_x + value
    #     # if self.get_player_location_x()
    
    # def set_player_location_y_2(self, value: int):
    #     self.__player_location_y = self.__player_location_y + value
    
    def add_hero_collection(self, value: Hero):
        self.__hero_owned.append(value)
        
    def add_hero_collection_by_dict(self, value: Hero):
        # self.__hero_owned_by_dict.append(value)
        self.__hero_owned_by_dict.update({value.get_name(): {"hero":value}})
        
    # def player_input(self, key, current_map):
    #     # print(f"{type(key.char)}")
    #     # print(f"Key type: {type(key)}")
    #     try:
    #         if key.char == 'p':
    #             print('Pause Menu')
    #             print('[1] Continue Game')
    #             print('[2] Get owned heroes by dict')
    #             print('[3] Exit Game')
    #             choose_menu = input("Choose menu: ")
    #             if choose_menu == '1':
    #                 print("Hello world from menu 1")
    #             elif choose_menu == '2':
    #                 print("Hello world from menu 2")
    #             else:
    #                 print("Hello world from menu 3")
                
    #         if key.char == 'q':
    #             print('Hello world from q')
    #     except AttributeError:
    #         pass
    #     if key == Key.right:
    #         self.__player_location_x = self.__player_location_x + 1
    #         if self.get_player_location_x() > current_map.get_width():
    #             self.__player_location_x = current_map.get_width()
    #         # self.set_player_location_x(1)
    #         # self.x_pos = self.x_pos + 1
            
    #     if key == Key.left:
    #         self.__player_location_x = self.__player_location_x - 1
    #         # self.x_pos = self.x_pos - 1
    #         if self.get_player_location_x() <0:
    #             self.__player_location_x = 0
                
    #     if key == Key.up:
    #         self.__player_location_y = self.__player_location_y + 1
    #         if self.get_player_location_y() > current_map.get_height():
    #             self.__player_location_y = current_map.get_height()
            
    #     if key == Key.down:
    #         self.__player_location_y = self.__player_location_y - 1
    #         # self.y_pos = self.y_pos - 1
    #         if self.get_player_location_y() < 0:
    #             self.__player_location_y = 0
        
    #     # clear_screen(0)
    #     print(f"x_pos⏳: {str(self.get_player_location_x())}, y_pos: {str(self.get_player_location_y())}",end='\r')
        
    def player_input(self, key, current_map):
        # print(f"{type(key.char)}")
        # print(f"Key type: {type(key)}")
        try:
            if key.char == 'p':
                print('Pause Menu')
                print('[1] Continue Game')
                print('[2] Get owned heroes by dict')
                print('[3] Exit Game')
                choose_menu = input("Choose menu: ")
                if choose_menu == '1':
                    print("Hello world from menu 1")
                elif choose_menu == '2':
                    print("Hello world from menu 2")
                else:
                    print("Hello world from menu 3")
                
            if key.char == 'q':
                print('Hello world from q')
        except AttributeError:
            pass
        if key == Key.right:
            self.__player_location_x = self.__player_location_x + 1
            if self.get_player_location_x() > current_map.get_width():
                self.__player_location_x = current_map.get_width()
            # self.set_player_location_x(1)
            # self.x_pos = self.x_pos + 1
            
        if key == Key.left:
            self.__player_location_x = self.__player_location_x - 1
            # self.x_pos = self.x_pos - 1
            if self.get_player_location_x() <0:
                self.__player_location_x = 0
                
        if key == Key.up:
            self.__player_location_y = self.__player_location_y + 1
            if self.get_player_location_y() > current_map.get_height():
                self.__player_location_y = current_map.get_height()
            
        if key == Key.down:
            self.__player_location_y = self.__player_location_y - 1
            # self.y_pos = self.y_pos - 1
            if self.get_player_location_y() < 0:
                self.__player_location_y = 0
        
        # clear_screen(0)
        print(f"current map: {current_map}")
        print(f"x_pos⏳: {str(self.get_player_location_x())}, y_pos: {str(self.get_player_location_y())}",end='\r')