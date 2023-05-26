class Character():
    def __init__(self, name: str = "", role: str = "", type: str ="",
                 current_hp: int = 0, max_hp: int =0, armor: int = 0, 
                 basic_attack_damage: int =0):
        self.__name = name
        self.__role = role
        self.__type = type
        self.__max_hp = max_hp
        self.__current_hp = current_hp
        self.__armor = armor
        self.__basic_attack_damage = basic_attack_damage        
    
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
        
    def get_role(self):
        return self.__role
    
    def set_role(self, value: int):
        role = {
            1 : "Monster",
            2 : "Hero"
        }
        self.__role = role[value]
    
    def get_type(self):
        return self.__type
    
    def get_current_hp(self):
        return self.__current_hp
    
    def set_current_hp(self, value):
        if self.__current_hp + value >= self.get_max_hp():
            self.__current_hp = self.get_max_hp()
        else:
            self.__current_hp = self.__current_hp + value
    
    def get_max_hp(self):
        return self.__max_hp
    
    def get_armor(self):
        return self.__armor
    
    def set_armor(self, value):
        self.__armor = value

    def get_basic_attack_damage(self):
        return self.__basic_attack_damage
    
    def set_basic_attack_damage(self, value: int):
        self.__basic_attack_damage = value
        
    