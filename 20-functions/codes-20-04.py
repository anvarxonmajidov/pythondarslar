"""

Dasturlash asoslari

#FUNCTIONS (FUNKSIYALAR)

#Muallif: Anvarxon Majidov amaliyot
"""

def oraliq(min, max):
    sonlar = []
    while min < max:
        sonlar.append(min)
        min += 1
    return sonlar


print(oraliq(0, 10))
print(oraliq(10, 21))

def oraliq(min,max,qadam=1):
    sonlar = []
    while min<max:
        sonlar.append(min)
        min += qadam
    return sonlar

print(oraliq(0,21,2))
