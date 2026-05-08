import os
import openpyxl
import pandas as pd
from pandas import DataFrame
#from xlwt import Workbook
#file1 = open(r"C:\Users\danie\Documents\romhacking\pokefireredtweaks\src\data\pokemon\species_info.h", "r")
#file2 = open(r"C:\Users\danie\Documents\romhacking\pokefireredtweaks\src\data\pokemon\charted_species_info.xlsx", "w")



__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

file1 = open(os.path.join(__location__, "species_info.h"), "r")
file2 = open(os.path.join(__location__, "charted_species_info.xlsx"), "w")

#This below four lines skip past the first chunk of the file that won't be used
row_counter = 0
while row_counter < 37:
    file1.readline()
    row_counter += 1

def grab_stats():
    # this section gets a mon's name
    # read 13 gets to the name of the mon in each string
    file1.read(13)
    mon_name = ""
    temp = ""
    base_hp = ""
    base_atk = ""
    base_def = ""
    base_spatk = ""
    base_spdef = ""
    base_speed = ""
    type_1 = ""
    type_2 = ""
    ability_1 = ""
    ability_2 = ""
    while temp != "]":
        temp = file1.read(1)
        if temp != "]":
            mon_name += temp
    mon_name_list.append(mon_name)

    # this section gets a mon's base stats

    # base hp
    # read two lines to get to the start of the base hp line
    file1.readline()
    file1.readline()
    while temp != "=":
        temp = file1.read(1)
    # read one more character to get past the space after the "="
    file1.read(1)
    # read until you hit the comma
    while temp != ",":
        temp = file1.read(1)
        if temp != ",":
            base_hp += temp
    mon_base_hp_list.append(base_hp)

    # base atk
    # read one line to get to the start of the base atk line
    file1.readline()
    while temp != "=":
        temp = file1.read(1)
    # read one more character to get past the space after the "="
    file1.read(1)
    # read until you hit the comma
    while temp != ",":
        temp = file1.read(1)
        if temp != ",":
            base_atk += temp
    mon_base_atk_list.append(base_atk)

    # base def
    # read one line to get to the start of the base def line
    file1.readline()
    while temp != "=":
        temp = file1.read(1)
    # read one more character to get past the space after the "="
    file1.read(1)
    # read until you hit the comma
    while temp != ",":
        temp = file1.read(1)
        if temp != ",":
            base_def += temp
    mon_base_def_list.append(base_def)

    # base speed
    # read one line to get to the start of the base speed line
    file1.readline()
    while temp != "=":
        temp = file1.read(1)
    # read one more character to get past the space after the "="
    file1.read(1)
    # read until you hit the comma
    while temp != ",":
        temp = file1.read(1)
        if temp != ",":
            base_speed += temp
    mon_base_speed_list.append(base_speed)

    # base spatk
    # read one line to get to the start of the base spatk line
    file1.readline()
    while temp != "=":
        temp = file1.read(1)
    # read one more character to get past the space after the "="
    file1.read(1)
    # read until you hit the comma
    while temp != ",":
        temp = file1.read(1)
        if temp != ",":
            base_spatk += temp
    mon_base_spatk_list.append(base_spatk)

    # base spdef
    # read one line to get to the start of the base spdef line
    file1.readline()
    while temp != "=":
        temp = file1.read(1)
    # read one more character to get past the space after the "="
    file1.read(1)
    # read until you hit the comma
    while temp != ",":
        temp = file1.read(1)
        if temp != ",":
            base_spdef += temp
    mon_base_spdef_list.append(base_spdef)

    # getting types
    # getting primary type
    file1.readline()
    while temp != "{":
        temp = file1.read(1)
    while temp != ",":
        temp = file1.read(1)
        if temp != ",":
            type_1 += temp
    mon_type_1_list.append(type_1)

    # getting secondary type
    file1.read(1)
    while temp != "}":
        temp = file1.read(1)
        if temp != "}":
            type_2 += temp
    mon_type_2_list.append(type_2)

    # getting abilities
    # getting first ability
    for i in range(16):
        file1.readline()
    while temp != "{":
        temp = file1.read(1)
    while temp != ",":
        temp = file1.read(1)
        if temp != ",":
            ability_1 += temp
    mon_ability_1_list.append(ability_1)

    # getting second ability
    file1.read(1)
    while temp != "}":
        temp = file1.read(1)
        if temp != "}":
            ability_2 += temp
    mon_ability_2_list.append(ability_2)

    # skip the end of the line after that and the rest of the mon's statblock to get to the next mon 
    for x in range(0,5):
        file1.readline()

# This block gets through gens 1+2, the unown break things, so I need to skip some lines to get the gen 3 mons
mon_name_list = []
mon_base_hp_list = []
mon_base_atk_list = []
mon_base_def_list = []
mon_base_spatk_list = []
mon_base_spdef_list = []
mon_base_speed_list = []
mon_type_1_list = []
mon_type_2_list = []
mon_ability_1_list = []
mon_ability_2_list = []
while len(mon_name_list) < 251:
    grab_stats()
    # # this section gets a mon's name
    # # read 13 gets to the name of the mon in each string
    # file1.read(13)
    # mon_name = ""
    # temp = ""
    # base_hp = ""
    # while temp != "]":
    #     temp = file1.read(1)
    #     if temp != "]":
    #         mon_name += temp
    # mon_name_list.append(mon_name)
    # # this section gets a mon's base stats
    # # read two lines to get to the start of the base hp line
    # file1.readline()
    # file1.readline()
    # while temp != "=":
    #     temp = file1.read(1)
    # # read one more character to get past the space after the "="
    # file1.read(1)
    # # read until you hit the comma
    # while temp != ",":
    #     temp = file1.read(1)
    #     if temp != ",":
    #         base_hp += temp
    # mon_base_hp_list.append(base_hp)
    # # skip the end of the line after the name and the rest of the mon's statblock to get to the next mon 
    # for x in range(0,27):
    #     file1.readline()
# skipping the unown lines
for x in range(0,25):
    file1.readline()
# grabbing the gen 3 mons
while len(mon_name_list) < 386:
    grab_stats()
# At this point, all pokemon names should be in the list mon_name_list
# print(mon_name_list, mon_base_hp_list)

# Trying using a pandas DataFrame to export it to excel
df = DataFrame({
    'Name': mon_name_list,
    'Base HP': mon_base_hp_list,
    'Base Attack': mon_base_atk_list,
    'Base Defense': mon_base_def_list,
    'Base Special Attack': mon_base_spatk_list,
    'Base Special Defense': mon_base_spdef_list,
    'Base Speed': mon_base_speed_list,
    'Primary Type': mon_type_1_list,
    'Secondary Type': mon_type_2_list,
    'Ability 1': mon_ability_1_list,
    'Ability 2': mon_ability_2_list
    })
print(df)
# This does work, but it shows up in the main POKEFIREREDTWEAKS directory
df.to_excel('charted_species_info.xlsx', sheet_name='sheet1', index=False)

# Each pokemon entry is 29 lines
# counting the first line with the mons' names as line 0, i need lines:
# 0, 2-8, and 24



file1.close()
file2.close()