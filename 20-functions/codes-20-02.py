"""

Dasturlash asoslari

#FUNCTIONS (FUNKSIYALAR)

#Muallif: Anvarxon Majidov amaliyot
"""


def toliq_ism_yasa(ism, familiya, otasining_ismi=""):
    """Toliq isma qaytaruvchi funksiya"""
    if otasining_ismi:
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()


talaba1 = toliq_ism_yasa("olim", "hakimov")
talaba2 = toliq_ism_yasa("hakim", "olimov", "abrorovich")
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
