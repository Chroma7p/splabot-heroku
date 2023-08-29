import csv

class Weapon:
    def __init__(self, main, weapon_type, sub, special, point):
        self.main = main
        self.weapon_type = weapon_type
        self.sub = sub
        self.special = special
        self.point = point

    def __str__(self):
        return f"[{self.weapon_type}] **{self.main}** : {self.sub}, {self.special}, {self.point}pt"

def get_weapon_info(file_name = 'weapondata.csv'):
    weapon_list = []
    
    with open(file_name, mode='r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)  # Skip header row
        
        for row in csv_reader:
            weapon = Weapon(row[0], row[1], row[2], row[3], int(row[4]))
            weapon_list.append(weapon)
    
    return weapon_list

def extract_weapon_types(weapons):
    weapon_types = set()
    sub_types = set()
    special_types = set()
    
    for weapon in weapons:
        weapon_types.add(weapon.weapon_type)
        sub_types.add(weapon.sub)
        special_types.add(weapon.special)
    
    return list(weapon_types), list(sub_types), list(special_types)

def filter_weapons(weapons, weapon_type=None, sub_type=None, special_type=None, soft =False):
    filtered_weapons = []
    
    for weapon in weapons:
        if soft:
            if (weapon_type is None or weapon_type in weapon.weapon_type) and \
               (sub_type is None or sub_type in weapon.sub) and \
               (special_type is None or special_type in weapon.special):
                filtered_weapons.append(weapon)
        elif (weapon_type is None or weapon.weapon_type == weapon_type) and \
           (sub_type is None or weapon.sub == sub_type) and \
           (special_type is None or weapon.special == special_type):
            filtered_weapons.append(weapon)
        
    return filtered_weapons

def salmon_weapon_info(name):
    if name=="ランダム":
        return "**ランダム**"
    if name=="はてな":
        return "**不明**"
    print(f"searching {name}")
    weapon_list = get_weapon_info()
    weapon = [weapon for weapon in weapon_list if weapon.main == name]
    return f"[{weapon[0].weapon_type}] **{weapon[0].main}**"