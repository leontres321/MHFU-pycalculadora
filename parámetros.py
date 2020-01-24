#armas :
#shield and sword
shield_n_sword_types = {"Regular Combo" : .46, "Revolving Slice" : .27, "Jumping Slice" : .18, "Rolling Slice" : .15, "Guard Attack 1" : .15, "Guard Attack 2" : .14, "Unsheathe Attack" : .18}

shield_n_sword_dict = {"Var" : {"All": 1} , "Type" : shield_n_sword_types, "Class" : 1.4}

#Dual Swords (DS)
dual_sword_types = {"Regular Combo" : .72, "Revolving Slice" : .31, "Charging Slice" : .23, "Rolling Slice" : .19, "Unsheathe attack" : .23 }

dual_sword_dict = {"Var" :{"All": .7}, "Type" : dual_sword_types, "Class" : 1.4}

# Lance
lance_types = {"Normal Stab Combo" : .76,"Upward Stab Combo" : .86, "Charge Through" : .20, "Charging Stab Finisher" : .40, "Guard Attack": .20,  "Unsheathe attack" : .28}

lance_dict = {"Var" : {"Normal Stab Combo" :.72, "Upward Stab Combo" : .72, "Unsheathe attack" : .72, "Charging Cut" : 1.12, "Charging Impact" : 0.81}, "Type" : lance_types, "Class" : 2.3}

# Gunlance (GL)
gun_lance_types = {"Normal Stab Combo" : .82,"Upward Stab Combo" : .54, "Rushing Stab" : .34, "Upward Swing": .30,  "Unsheathe attack" : .34}

gunlance_dict = {"Var" : {"All": .95}, "Type" : gun_lance_types, "Class" : 2.3}

#Great Sword (GS)
great_sword_types = {"Regular Slice" : .48, "Sideways Slash" : .36, "Upswing" : .46, "Level 1 Charge" : .65, "Level 2 Charge" : .80, "Level 3 Charge" : 1.10, "Unsheathe attack" : .48 }

great_sword_dict = {"Var" : {"Center" : 1.05, "Level 1" : 1.1, "Level 2" : 1.2, "Level 3" : 1.3}, "Type" : great_sword_types, "Class" : 4.8}

# Long Sword (LS)
long_sword_types = {"Forward Slice" : .61, "Piercing Stab" : .20, "Sweeping Slice" : .30, "Upward Slice" : .23, "Downward Slice" : .28, "No Spirit Attack" : .16, "Spirit Attack" : 1.47, "Unsheathe Attack" : .33 }

long_sword_dict = {"Var" : {"Center" : 1.05, "Spirit Gauge" : 1.12}, "Type" : long_sword_types, "Class" : 4.8}

#  Hammer
hammer_types = {"Regular Combo" : 1.72, "Side Swing" : .15, "Spinning Attack" : .40, "Short Charge" : .45, "Medium Charge" : .80, "Superpound" : .96, "Unsheathe attack" : .20}

hammer_dict = {"Var" :{"All": 1}, "Type" : long_sword_types, "Class" : 5.2}

#Hunting Horn (HH)
hunting_horn_types = {"Swing Attack" : .27, "Poke Attack" : .36, "Overhead Smash" : .63, "Unsheathe attack" : .27 }

hunting_horn_dict = {"Var" : {"All": 1}, "Type" : long_sword_types, "Class" : 5.2}


divisor = 10

#### formato hitzone :[["Cabeza", .50, .60, .0 ,.05 ,.20, .40, .0],...]
hit_dict = {"Cut" : 1, "Impact" : 2, "Fire" : 3, "Water" : 4,"Thunder" : 5, "Dragon" : 6, "Ice" : 7}

base_sharp = {"rojo": 0.5, "naranjo": 0.75, "amarillo": 1, "verde": 1.125, "azul": 1.25, "blanco": 1.3, "morado": 1.5}
elemental_sharp = {"rojo": 0.25, "naranjo": 0.5, "amarillo": 0.75, "verde": 1, "azul": 1.0625, "blanco": 1.125, "morado": 1.2}





