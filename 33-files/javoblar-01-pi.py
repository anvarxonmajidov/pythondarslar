"""
#33-DARS.FILES

Muallif:ANVARXON MAJIDOV AMALIYOT


"""


# import pickle

with open("amaliyot/pi_million_digits.txt") as file:
    pi = file.read()
pi = pi.rstrip()  # qator ohiridagi bo'shliqlarni olib tashlaymiz
pi = pi.replace("\n", "")  # qator tashlash belgisini almashtiramiz
pi = pi.replace(" ", "")

# Tug'ilgan kunim pi da bormi?
bdate = "31122000"
print(bdate in pi)

# pi = float(pi) # matnni float (o'nlik) songa o'tkazamiz

# with open('amaliyot/pi_float.dat','wb') as file:
#     pickle.dump(pi,file)
