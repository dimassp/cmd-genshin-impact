import time
from maps.maps import maps, maps_2 , Maps
from character.monster.monster import monster_list_2
from utilities import write_per_character, clear_screen
map_list = [
    {
        "name": "Tevyat",
        "width": 15,
        "height": 30,
        "tiles" : {
            "10x10": {
                # "monsters": {
                #     "Cyro Slime": type(monster_list_2),
                #     "Dendro Slime": monster_list_2.get("Dendro Slime")
                # }
                "monsters": ["Cyro Slime", "Dendro Slime"]
            },
            "12x10": {
                "monsters": ["Dendro Slime", "Cyro Slime"]
            }
        }
        # "width": 15,
        # "height": 30,
    },
    {
        "name": "Enkanomiya",
        # "width": 12,
        # "height": 29,
        "width": 12,
        "height": 29,
    },
    {
        "name": "Serenitea Pot",
        "width": 15,
        "height": 30,
        "tiles" : {
            "10x10": {
                "monsters": ["Cyro Slime", "Dendro Slime"]
            },
            "12x10": {
                "monsters": ["Dendro Slime", "Cyro Slime"]
            },
            
        }
        # "width": 15,
        # "height": 30,
    },
]

def print_maps():
    print()
    for i, map in enumerate(maps_2):
        # write_per_character(f"{i+1}. {map['name']}", 0.03, 0.3)
        write_per_character(f"{i+1}. {map}", 0.03, 0.3)
        print()
        
def choose_maps():
    
    print_maps()
    write_per_character("Choose map: ", 0.03, 0)
    choose_maps_var = input("")
    choose_maps_var = int(choose_maps_var)
    selected_map_name = ""
    
    try:
        selected_map_name = list(maps_2)[choose_maps_var-1]
    except:
        pass
    
    while not choose_maps_var >=1 or not choose_maps_var <= len(maps_2):
        if not choose_maps_var >=1 or not choose_maps_var <= len(maps_2):
            clear_screen(0)
            write_per_character(f"There are only {len(maps_2)} maps. Please select from 1 to {len(maps_2)}", 0.03, 0)
            print_maps()
            write_per_character("\nChoose map: ", 0.03, 0)
            choose_maps_var = input("")
            choose_maps_var = int(choose_maps_var)
        else:
            selected_map_name = list(maps_2)[choose_maps_var-1]
            return maps_2.get(selected_map_name)
        
    if choose_maps_var >=1 or choose_maps_var <= len(maps_2):
        return maps_2.get(selected_map_name)
    # else:
    #     print("Break while")
def generate_maps():

    for map in map_list:
        new_map = Maps(map['name'], map['width'], map['height'])
        try:
            for tile_location in map['tiles']:
                # print(f"tile location: {tile_location}")
                new_map.set_tiles({tile_location: map['tiles'][tile_location]})

        except KeyError:
            pass
        maps.append({'name': map["name"], 'map': new_map})
        maps_2.update({map['name']: new_map})