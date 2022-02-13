"""
#34-DARS. JSON

Muallif:ANVARXON MAJIDOV AMALIYOT

"""

while True:
    book = input("Yaxshi koʻrgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
    if not book:
        break
    with open("amaliyot/books.txt", "a") as file:
        file.write(book + "\n")
