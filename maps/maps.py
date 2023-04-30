maps = list()

class Maps():
    def __init__(self, name: str, width: int, height: int):
        self.__name = name
        self.__width = width
        self.__height = height
    
    def get_width(self):
        return self.__width
    
    def get_name(self):
        return self.__name
    
    def get_height(self):
        return self.__height
    
        