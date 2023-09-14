import requests
from bs4 import BeautifulSoup

response=requests.get("https://bank.gov.ua")
if response.status_code==200:
    bs=BeautifulSoup(response.text, features="html.parser")
    eur=bs.find_all("div", {"class":"value-full"})
    print(f"Эвро={eur[0].text}")
    print(f"Долар={eur[1].text}")