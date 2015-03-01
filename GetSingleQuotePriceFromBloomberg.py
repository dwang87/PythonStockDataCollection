# -*- coding: utf-8-*-
# @Date    : 2015-02-20
# @Author  : Chris
# @Website : 
# @Description:  Get prices from Bloomberg
# @Tools-Required: re, urllib
import urllib
import re
import json

htmltext = urllib.urlopen("http://www.bloomberg.com/markets/watchlist/recent-ticker/AAPL:US")

data = json.load(htmltext)

print data['last_price']
