#!/usr/bin/python
# encoding: utf-8
import urllib2,cookielib
import bs4 as bs
import random
from time import sleep

d_site = "https://www.google.com.tr/search?q=1+usd+to+try&oq=1+usd+to+try&aqs=chrome..69i57.1655j0j1&sourceid=chrome&ie=UTF-8"
e_site = "https://www.google.com.tr/search?q=1+euro+to+try&oq=1+euro+to+try&aqs=chrome..69i57.1639j0j1&sourceid=chrome&ie=UTF-8"
p_site = "https://www.google.com.tr/search?q=1+gbp+to+try&oq=1+gbp+to+try&aqs=chrome..69i57.2388j0j1&sourceid=chrome&ie=UTF-8"
c_site = "https://www.google.com.tr/search?q=1+cad+to+try&oq=1+cad+to+try&aqs=chrome..69i57.2198j0j9&sourceid=chrome&ie=UTF-8"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Connection': 'keep-alive'}

d_req = urllib2.Request(d_site, headers=hdr)
e_req = urllib2.Request(e_site, headers=hdr)
p_req = urllib2.Request(p_site, headers=hdr)
c_req = urllib2.Request(c_site, headers=hdr)


try:
    d_page = urllib2.urlopen(d_req)
    e_page = urllib2.urlopen(e_req)
    p_page = urllib2.urlopen(p_req)
    c_page = urllib2.urlopen(c_req)
except urllib2.HTTPError, e:
    print "Sorry, the page is down, please contact Kaan."

d_content = d_page.read()
d_soup = bs.BeautifulSoup(d_content, "lxml")
e_content = e_page.read()
e_soup = bs.BeautifulSoup(e_content, "lxml")
p_content = p_page.read()
p_soup = bs.BeautifulSoup(p_content, "lxml")
c_content = c_page.read()
c_soup = bs.BeautifulSoup(c_content, "lxml")



dollar = round(float(str(d_soup.find(class_="dDoNo vk_bk"))[25:-20]),2)
euro = round(float(str(e_soup.find(class_="dDoNo vk_bk"))[25:-20]),2)
pound = round(float(str(p_soup.find(class_="dDoNo vk_bk"))[25:-20]),2)
cad = round(float(str(c_soup.find(class_="dDoNo vk_bk"))[25:-20]),2)

print("USD: " + str(dollar))
print("EUR: " + str(euro))
print("GBP: " + str(pound))
print("CAD: " + str(cad))
