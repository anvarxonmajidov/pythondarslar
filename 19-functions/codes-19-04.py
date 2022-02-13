"""

Dasturlash asoslari

#FUNCTIONS (FUNKSIYALAR)

#Muallif: Anvarxon Majidov amaliyot
"""


def yosh_hisobla(tugilgan_yil, joriy_yil):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")


yosh_hisobla(1995,2022)
yosh_hisobla(1999)

tyil = input("Tug'ilgan yilingizni kiriting: ")
yosh_hisobla(tyil)
