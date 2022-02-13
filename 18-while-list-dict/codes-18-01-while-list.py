

# WHILE VA RO'YXATLAR

#Muallif: Anvarxon Majidov amaliyot

print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
ismlar = []
n = 1  # ismlarni sanash uchun o'zgaruvchi
while True:
    savol = f"{n}-do'stingiz ismini kiriting:"
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
    n += 1
    if takrorlash != "ha":
        break


print("Do'stlaringiz ro'yxati:")
for ism in ismlar:
    print(ism.title())
