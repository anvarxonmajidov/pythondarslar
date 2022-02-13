"""
#*args va **kwargs

#Muallif: Anvarxon Majidov amaliyot

"""
def multiply(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma


print(multiply(4, 5, 6))
