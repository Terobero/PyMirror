#!/usr/bin/python
# encoding: utf-8
import urllib2,cookielib
import bs4 as bs
import random
from time import sleep

site= "https://www.wikizero.com/tr/"
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


column = soup.find_all(class_="MainPageBG")[1]

unicode =  u'' + column.text
unicode_start = unicode.index(u"Olaylar")
unicode_end = unicode.index(u"Doğumlar")

start_index = 0
events = unicode[unicode_start:unicode_end]
event_list = []

skip = 0

for i in range(len(events)):
    if events[i].isdigit():
        start_index = i
        break
start = start_index
for i in range(start, len(events)):
    year_len = 0
    if skip > 0:
        skip -= 1
        continue
    
    while True:
        if events[i].isdigit():
            year_len += 1
            i += 1
        elif events[i:i+3] == " - " and events[i+3].isupper():
            event_list.append(events[start_index:i-year_len])
            start_index = i-year_len
            skip = 4
            break
        else:
            break

event_list.append(events[start_index:])
event_list.pop(0)

for event in event_list:
    event.rstrip()
    
while True:
    print event_list[random.randint(0, len(event_list)-1)]
    print
    sleep(2)
