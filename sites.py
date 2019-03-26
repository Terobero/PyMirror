#!/usr/bin/python
# encoding: utf-8
import urllib2,cookielib
import bs4 as bs
from datetime import datetime

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Connection': 'keep-alive'}

# Weather - BBC Weather
site_weather = "https://weather-broker-cdn.api.bbci.co.uk/en/observation/rss/745044"
req_weather = urllib2.Request(site_weather, headers=hdr)

# News - Anadolu Ajansı
site_news = "https://www.aa.com.tr/tr/rss/default?cat=guncel"
req_news = urllib2.Request(site_news, headers=hdr)

# Money - Doviz.com
site_money = "https://m.doviz.com"
req_money = urllib2.Request(site_money, headers=hdr)

def getWeatherData(req_weather):
    try:
        page = urllib2.urlopen(req_weather)
    except urllib2.HTTPError, e:
        print "Failed to update WEATHER on " + str(datetime.now())
        return
    file = open("weather.txt", "r")
    prev_weather_state = file.read().split("/|/")[0]
    file.close()
    file = open("weather.txt", "w")
    content = page.read()
    soup = bs.BeautifulSoup(content, "lxml").find("item")
    title = soup.find("title").text
    weather_state, temp = title[title.index("EET:")+5:title.index(" (")].split(", ")
    if weather_state == "Not available": weather_state = prev_weather_state
    description = soup.find("description").text
    humidity = description[description.index("Humidity:")+10:description.index("%, Pressure")]
    file.write(weather_state + "/|/" + temp + "/|/%" + humidity)
    file.close()
    
def getNewsData(req_news):
    try: page = urllib2.urlopen(req_news)
    except urllib2.HTTPError, e:
        print "Failed to update NEWS on " + str(datetime.now())
        return
    file = open("news.txt", "w")
    content = page.read()
    soup = bs.BeautifulSoup(content, "lxml")
    news = soup.find_all("title")
    altered_news = []
    # This is to remove clickbaits & non-news
    for new in news:
        if "?" not in str(new) and "..." not in str(new) and "60 saniyede bugün" not in str(new) and "Anadolu Ajansı Güncel Haberler" not in str(new):
            altered_news.append(str(new)[7:-8])
    for new in altered_news:
        file.write(new)
        file.write("/|/")
    file.close()

def getMoneyData(req_money):
    try: page = urllib2.urlopen(req_money)
    except urllib2.HTTPError, e:
        print "Failed to update MONEY on " + str(datetime.now())
        return()
    file = open("money.txt", "w")
    content = page.read()
    soup = bs.BeautifulSoup(content, "lxml")
    usd = soup.find("li", {"data-table-homepage-key":"USD"})
    usd = str(round(float(usd.find_all("div", {"class":"row4"})[-1].text.replace(",",".")),2))
    eur = soup.find("li", {"data-table-homepage-key":"EUR"})
    eur = str(round(float(eur.find_all("div", {"class":"row4"})[-1].text.replace(",",".")),2))
    gbp = soup.find("li", {"data-table-homepage-key":"GBP"})
    gbp = str(round(float(gbp.find_all("div", {"class":"row4"})[-1].text.replace(",",".")),2))
    cad = soup.find("li", {"data-table-homepage-key":"CAD"})
    cad = str(round(float(cad.find_all("div", {"class":"row4"})[-1].text.replace(",",".")),2))
    ceyrek = soup.find("a", {"href":"//m.doviz.com/altin/ceyrek-altin"})
    ceyrek = str(round(float(ceyrek.find_all("div", {"class":"row4"})[-1].text.replace(",",".")),2))
    yarim = soup.find("a", {"href":"//m.doviz.com/altin/yarim-altin"})
    yarim = str(round(float(yarim.find_all("div", {"class":"row4"})[-1].text.replace(",",".")),2))
    file.write(usd + " " + eur + " " + gbp + " " + cad + " " + ceyrek + " " + yarim)
    file.close()