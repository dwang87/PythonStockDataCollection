# -*- coding: utf-8-*-
# @Date    : 2015-02-20
# @Author  : Chris
# @Website : 
# @Description:  Get prices from Google Finance
# @Tools-Required: re, urllib
import urllib
import re


htmlfile = urllib.urlopen("http://www.google.com/finance/getprices?q=GOOG&x=NASD&i=10&p=25m&f=c")
htmltext = htmlfile.read()

print htmltext.split()[len(htmltext.split())-1]
