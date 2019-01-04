from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

import pandas as pd

df = pd.DataFrame(columns = ["Total", "Night", "Noon", "JA", "EN", "url"])
page = 59
while True:

    url = "https://tabelog.com/tw/tokyo/rstLst/" + str(page) + "/?SrtT=rt"
    print("正在處理url", url)

    try:
        response = urlopen(url)
    except HTTPError:
        print( "這應該是最後一頁了")
        break

    html = BeautifulSoup(response)

    #find (找第一個符合的條件), find_all(找所有符合的條件)

    #print(html.find_all('li', {"class": "list-rst"}))
    for r in html.find_all('li', class_="list-rst"):
        ja = r.find("small", class_ = "list-rst__name-ja")
        en = r.find("a", class_="list-rst__name-main")
        ratings = r.find_all("b", class_="c-rating__val")
        #萃取紙條(.text) 萃取特別特徵([特徵])
        print(ratings[0].text,
              ratings[1].text,
              ratings[2].text,
              ja.text,
              en.text,
              en["href"])
        s = pd.Series([ratings[0].text, ratings[1].text,ratings[2].text, ja.text, en.text, en["href"]],
            index= ["Total", "Night", "Noon", "JA", "EN", "url"])
        df = df.append(s, ignore_index=True)
    page = page + 1
#PD
df.to_csv("tabelog.csv", encoding = "utf-8", index = False)