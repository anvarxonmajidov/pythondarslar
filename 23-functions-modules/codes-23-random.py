"""
# modullar

#Muallif: Anvarxon Majidov amaliyot

"""
import random as r

#randint()
son = r.randint(10,50)
print(son)

#choice()
ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar)
print(ism)
print(r.choice(ism))
x = list(range(0,51,5))
print(x)
print(r.choice(x))

#shuffle()
x = list(range(11))
print(x)
r.shuffle(x)
print(x)
