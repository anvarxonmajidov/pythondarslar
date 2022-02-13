"""
#35-DARS. XATOLAR BILAN ISHLASH

Muallif:ANVARXON MAJIDOV AMALIYOT

"""

while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break

print(f"Siz {2021-yosh} yilda tug'ilgansiz")
