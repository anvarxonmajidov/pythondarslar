"""
#*args va **kwargs

#Muallif: Anvarxon Majidov amaliyot

"""

def talaba_info(ism, familiya, **kwargs):
    kwargs["ism"] = ism
    kwargs["familiya"] = familiya
    return kwargs


talaba = talaba_info("anvar", "majidov", tyil=2000, fakultet="SA", yonalish="ATT")
