from player.player import Player
from character.monster.monster import basic_monster_list_2
maps = list()
maps_2 = dict()

class Maps():
    def __init__(self, name: str, width: int, height: int):
        self.__name = name
        self.__width = width
        self.__height = height
        self.tiles ={
            "tiles": {}
        }
        self.__player: Player =None
        
    def get_width(self):
        return self.__width
    
    def get_name(self):
        return self.__name
    
    def get_height(self):
        return self.__height
    
    def get_tiles(self):
        return self.tiles
    
    def set_tiles(self, value: dict):
        self.tiles['tiles'].update(value)
    
    def get_player(self):
        return self.__player
    
    def set_player(self, value: Player|None):
        self.__player = value
        