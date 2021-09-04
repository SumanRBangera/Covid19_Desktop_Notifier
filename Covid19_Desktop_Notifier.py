#using webscrapping

from urllib.request import urlopen, Request    ##for fetching and opening url
from bs4 import BeautifulSoup as bs         ##for pulling data
from plyer import notification    ##notification
import time

header = {"User-Agent":"Mozilla"}
req = Request("https://www.worldometers.info/coronavirus/country/india/",headers = header)
html = urlopen(req)

print(html.status)

obj = bs(html,"html.parser")
new_cases = obj.find("li",{"class":"news_li"}).strong.text.split()[0]
death = list(obj.find("li",{"class":"news_li"}).strong.next_siblings)[1].text.split()[0]

def notifyme(notify_title, newcases, deaths):
    notification.notify(title = notify_title,
                       message =  "New Cases - "+ newcases+"\nDeaths - "+deaths,
                        timeout = 5)
                        

while True:
    notifyme("Covid-19 Update", new_cases, death)
    time.sleep(10)

