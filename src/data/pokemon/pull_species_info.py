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


# This block gets through gens 1+2, the unown break things, so I need to skip some lines to get the gen 3 mons
mon_name_list = []
while len(mon_name_list) < 251:
    # read 13 gets to the name of the mon in each string
    file1.read(13)
    mon_name = ""
    temp = ""
    while temp != "]":
        temp = file1.read(1)
        if temp != "]":
            mon_name += temp
    mon_name_list.append(mon_name)
    for x in range(0,29):
        file1.readline()
# skipping the unown lines
for x in range(0,25):
    file1.readline()
# grabbing the gen 3 mons
while len(mon_name_list) < 386:
    # read 13 gets to the name of the mon in each string
    file1.read(13)
    mon_name = ""
    temp = ""
    while temp != "]":
        temp = file1.read(1)
        if temp != "]":
            mon_name += temp
    mon_name_list.append(mon_name)
    for x in range(0,29):
        file1.readline()
# At this point, all pokemon names should be in the list mon_name_list
# print(mon_name_list)

# Trying using a pandas DataFrame to export it to excel
df = DataFrame({'Name': mon_name_list})
print(df)
# This no work for some reason :(
df.to_excel('charted_species_info.xlsx', sheet_name='sheet1', index=False)

# Each pokemon entry is 29 lines
# counting the first line with the mons' names as line 0, i need lines:
# 0, 2-8, and 24


file1.close()
file2.close()