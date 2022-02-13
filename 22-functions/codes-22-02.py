"""
#*args va **kwargs

#Muallif: Anvarxon Majidov amaliyot

"""

def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return sum(sonlar)


print(summa(2))
print(summa(1, 2, 3, 4, 5))
print(summa(4, 5, 6, 7))
