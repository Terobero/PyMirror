#!/usr/bin/python
# encoding: utf-8
import urllib2,cookielib
import bs4 as bs
from datetime import datetime

#Anadolu Ajansı
site= "https://www.aa.com.tr/tr/rss/default?cat=guncel"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Connection': 'keep-alive'}

req = urllib2.Request(site, headers=hdr)


try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print "Failed to update NEWS on " + str(datetime.now())
    quit()

file = open("news.txt", "w")

content = page.read()
soup = bs.BeautifulSoup(content, "lxml")


news = soup.find_all("title")
altered_news = []

#This is to remove clickbaits & non-news
for new in news:
    if "?" not in str(new) and "..." not in str(new) and "60 saniyede bugün" not in str(new) and "Anadolu Ajansı Güncel Haberler" not in str(new):
        altered_news.append(str(new)[7:-8])

for new in altered_news:
    file.write(new)
    file.write("\n")

file.close()