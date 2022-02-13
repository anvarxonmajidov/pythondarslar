"""

#24-dars: FUNKSIYALAR SO'NGSO'Z

Muallif: Anvarxon Majidov amaliyot


"""
import math

def nom(argument):
    return nom

uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))

kvadrat = lambda x, y : x ** y
print(kvadrat(3, 2))


def daraja(n):
    return lambda x: x ** n


kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, " f"kubi {kub(3)} ga teng")
