"""
#33-DARS.FILES

Muallif:ANVARXON MAJIDOV AMALIYOT


"""

with open("pi.txt") as file:
    pi = file.read()

print(pi)

pi = pi.rstrip()
pi = pi.replace("\n", "")
pi = float(pi)
print(pi)


filename = "data/talabalar.txt"
with open(filename) as file:
    for line in file:
        print(line)

with open(filename) as file:
    talabalar = file.readlines()

print(talabalar)

talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)
