# -*- coding: utf-8-*-
# @Date    : 2015-05-20
# @Author  : Chris
# @Website : 
# @Description:  Get Apple price from Yahoo Finance
# @Tools-Required: re, urllib
import urllib
import re

symbolslist = ["aapl","spy","goog","nflx","qihu","yy"]

i=0
while i<len(symbolslist):
    htmlfile = urllib.urlopen("http://finance.yahoo.com/q?s="+symbolslist[i] +"&ql=1")
    htmltext = htmlfile.read()

    regex = '<span id="yfs_l84_'+symbolslist[i]+'">(.+?)</span>'

    pattern = re.compile(regex)

    price = re.findall(pattern, htmltext)

    print "the price of",symbolslist[i]," is ", price[0]
    i+=1