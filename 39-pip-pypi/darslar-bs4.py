"""

#39-DARS. PYTHON TASHQI KUTUBXONASI

Muallif: Anvarxon Majidov amaliyot

"""

import requests
from bs4 import BeautifulSoup


sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
# pprint(r.text)

soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())
news = soup.find_all(class_="news-title")
print(news[0].text)
