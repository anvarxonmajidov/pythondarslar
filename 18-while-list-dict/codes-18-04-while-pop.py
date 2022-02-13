
#WHILE VA RO'YXATLAR
#Muallif: Anvarxon Majidov amaliyot

talabalar = ["hasan", "husan", "olim", "botir"]
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = int(baho)
