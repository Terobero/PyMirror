#!/usr/bin/python
# encoding: utf-8
import urllib2,cookielib
import bs4 as bs
import random
from time import sleep

site= "http://www.gazetevatan.com/rss/gundem.xml"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Connection': 'keep-alive'}

req = urllib2.Request(site, headers=hdr)

try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print "Sorry, the page is down, please contact Kaan."

content = page.read()
soup = bs.BeautifulSoup(content, "lxml")


news = soup.find_all("item")
altered_news = []

#This is to remove clickbaits
for new in news:
    new = new.title
    if "?" not in str(new) and "..." not in str(new):
        altered_news.append(new)

for new in altered_news:
    new = str(new)[20:-15]

while True:
    print str(altered_news[random.randint(0, len(altered_news)-1)])[20:-15]
    print
    sleep(2)
