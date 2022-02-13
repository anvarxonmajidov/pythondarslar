# AMALIYOT Anvarxon Majidov

# LUG'AT ICHIDA RO'YXAT
dasturchilar = {
    "ali": ["python", "c++"],
    "vali": ["html", "css", "js"],
    "hasan": ["php", "sql"],
    "husan": ["python", "php"],
    "maryam": ["c++", "c#"],
}

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end="")
    for til in tillar:
        print(f"{til.upper()} ", end="")
