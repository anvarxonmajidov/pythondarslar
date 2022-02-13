"""


#38-DARS. PYTHON KUTUBXONASI

Muallif: ANVARXON MAJIDOV

"""
from pprint import pprint
import json

filename = "bemor.json"
with open(filename) as f:
    bemor = json.load(f)

# pprint(bemor)
pprint(bemor)

import requests

r = requests.get("https://api.github.com")

pprint(r.json())
