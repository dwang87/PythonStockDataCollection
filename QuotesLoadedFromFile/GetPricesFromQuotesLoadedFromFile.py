# -*- coding: utf-8-*-
# @Date    : 2015-05-20
# @Author  : Chris
# @Website : 
# @Description:  Get prices from quotes loaded from a text file
# @Tools-Required: re, urllib
import urllib
import re

symbolfile = open("symbols.txt")

symbolslist = symbolfile.read()

newsymbolslist = symbolslist.split("\n")


i=0
while i<len(newsymbolslist):
    #htmllink = "http://finance.yahoo.com/q?s="+newsymbolslist[i] +"&ql=1"
    #print htmllink
    htmlfile = urllib.urlopen("http://finance.yahoo.com/q?s="+newsymbolslist[i] +"&ql=1")
    htmltext = htmlfile.read()

    regex = '<span id="yfs_l84_'+newsymbolslist[i].lower()+'">(.+?)</span>'
   
    pattern = re.compile(regex)

    price = re.findall(pattern, htmltext)

    print "the price of",newsymbolslist[i]," is ", price[0]
    i+=1