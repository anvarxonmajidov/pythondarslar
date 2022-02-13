"""


#28-DARS. KLASSLAR

Muallif:MAJIDOV ANVARXON AMALIYOT


"""


class Talaba:
    """Talaba nomli klass yaratamiz"""

    def __init__(self, ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")


talaba1 = Talaba("Alijon", "Valiyev", 2000)
print(talaba1.ism)
print(talaba1.familiya)
talaba1.tanishtir()

talaba2 = Talaba("Olim", "Olimov", 1995)
talaba2.tanishtir()
talaba3 = Talaba("Husan", "Akbarov", 2004)
talaba4 = Talaba("Hasan", "Akbarov", 2004)
talaba4.tanishtir()
