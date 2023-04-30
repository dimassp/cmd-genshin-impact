from maps.maps import maps, Maps

map_list = [
    {
        "name": "Tevyat",
        "width": 1500,
        "height": 3000,
    },
    {
        "name": "Enkanomiya",
        "width": 1245,
        "height": 2900,
    },
]

def generate_maps():
    for map in map_list:
        new_map = Maps(map['name'], map['width'], map['height'])
        maps.append(new_map)