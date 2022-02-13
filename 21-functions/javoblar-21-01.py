"""

#funksiyaga ro'yhat uzatish

#Muallif: Anvarxon Majidov amaliyot
"""

def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()


ismlar = ["ali", "vali", "hasan", "husan"]
katta_harf(ismlar)
print(ismlar)
