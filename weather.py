#!/usr/bin/python
# encoding: utf-8
import urllib2,cookielib
from urllib import urlretrieve
import bs4 as bs
from datetime import datetime
from os import path
from PIL import Image

site= "https://www.google.com/search?q=istanbul+weather"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Connection': 'keep-alive'}

req = urllib2.Request(site, headers=hdr)


try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print "Failed to update WEATHER on " + str(datetime.now())
    quit()

file = open("weather.txt", "w")

content = page.read()
soup = bs.BeautifulSoup(content, "lxml")

weather = soup.find(class_="vk_c card-section")
weather_state = weather.find("div", {"id":"wob_dcp"}).text
degree = weather.find("span", {"class":"wob_t", "id":"wob_tm"}).text
image = weather.find("div", {"id":"wob_d"}).find("img")["src"]

urlretrieve("https:"+str(image), path.basename("weather_image.jpg"))
img = Image.open('weather_image.jpg').convert('LA')
img.save('grayscale.png')

file.write(str(weather_state) + "|" + str(degree))
file.close()