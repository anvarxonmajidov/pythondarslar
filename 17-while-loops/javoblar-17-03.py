# AMALIYOT Anvarxon Majidov

savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == "exit":
        break
    elif float(qiymat) < 0:
        continue  # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
    else:
        ildiz = float(qiymat) ** (0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
