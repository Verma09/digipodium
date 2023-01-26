import pandas as pd 
import requests
from bs4 import BeautifulSoup

for i in range(2,10):
    url = "https://www.flipkart.com/search?q=mobiles%20under%2050000%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

    r = requests.get(url)
# print(r)

    soup = BeautifulSoup(r.text, "lxml")
# print(soup)ds

# while True:
    np = soup.find('a', class_="ge-49M _2Kfbh8").get("href")
    cnp = "https://www.flipkart.com"+np
    print(cnp)



    # url = cnp
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text,"lxml")
