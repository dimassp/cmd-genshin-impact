import sys

from passlib.context import CryptContext
from character.hero.hero import Hero
# sys.path.append(r'D:\PROGRAMMING\python\bani\Genshin-Impact-OOP-master\New Genshin Impact')



PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

player_list = list()

class Player():
    def __init__(self, username: str, password: str, ):
        self.__username = username
        self.__password = PWD_CONTEXT.hash(password)
        self.__hero_owned = list()
    
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def get_hero_owned(self):
        return self.__hero_owned
    
    def add_hero_collection(self, value: Hero):
        self.__hero_owned.append(value)