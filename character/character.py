class Character():
    def __init__(self, name: str = "", role: str = "", hp: int = 0, 
                 armor: int = 0, basic_attack_damage: int =0, level: int =1, exp: int=0):
        self.__name = name
        self.__role = role
        self.__hp = hp
        self.__armor = armor
        self.__basic_attack_damage = basic_attack_damage
        self.__level = 1
        self.__exp = exp
    
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

    def get_hp(self):
        return self.__hp
    
    def set_hp(self, value):
        self.__hp = value

    def get_armor(self):
        return self.__armor
    
    def set_armor(self, value):
        self.__armor = value

    def get_basic_attack_damage(self):
        return self.__basic_attack_damage
    
    def set_basic_attack_damage(self, value: int):
        self.__basic_attack_damage = value
        
    def get_level(self):
        return self.__level
    
    def set_level(self, value: int):
        self.__level = self.__level + value
        
    def get_exp(self):
        return self.__exp
    
    def set_exp(self, value: int):
        self.__exp = value