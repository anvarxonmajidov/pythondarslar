"""

#funksiyaga ro'yhat uzatish

#Muallif: Anvarxon Majidov amaliyot
"""

talabalar = ["ali", "vali", "hasan", "husan"]


def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar


baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)
