import requests
from bs4 import BeautifulSoup

url=("www.google.com")
code=requests.get("https://"+url)

plain=code.text
s=BeautifulSoup(plain)

for link in s.find_all("a"):
 print(link.get("href"))
