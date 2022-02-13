"""
#33-DARS.FILES

Muallif:ANVARXON MAJIDOV AMALIYOT


"""

import pickle

with open("info", "rb") as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

print(talaba1)
print(talaba2)
