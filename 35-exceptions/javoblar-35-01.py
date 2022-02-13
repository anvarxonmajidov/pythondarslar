"""
#35-DARS. XATOLAR BILAN ISHLASH

Muallif:ANVARXON MAJIDOV AMALIYOT

"""

try:
    x = int(input("son kiriting: "))
    y = int(input("yana son kiriting: "))
    print(x, "/", y, "=", x / y)
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmaydi")
except ValueError:
    print("Bu son emas")
except:
    print("Xato yuz berdi!")
