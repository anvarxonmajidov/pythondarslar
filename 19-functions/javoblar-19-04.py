"""

Dasturlash asoslari

#FUNCTIONS (FUNKSIYALAR)

#Muallif: Anvarxon Majidov amaliyot
"""

# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
def solishtir(x, y):
    """Ikki sonni solishtiruvchi funksiya"""
    if x > y:
        print(f"{x}>{y}")
    elif x < y:
        print(f"{y}>{x}")
    else:
        print(f"{x}={y}")


solishtir(10, 20)
solishtir(-9, 12)
solishtir(1223 * 5, 5 ** 4)
