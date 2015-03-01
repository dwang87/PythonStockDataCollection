# -*- coding: utf-8-*-
# @Date    : 2015-02-20
# @Author  : Chris
# @Website : 
# @Description:  Get prices from Bloomberg
# @Tools-Required: re, urllib
import urllib
import re
import json

htmlfile= urllib.urlopen("http://www.sgx.com/proxy/SgxDominoHttpProxy?timeout=100&dominoHost=http%3A%2F%2Finfofeed.sgx.com%2FApps%3FA%3DCow_CorporateInformation_Content%26B%3DCorpDistributionByCompanyNameCategoryAndExYear%26R_C%3DSATS%20LTD.%26C_T%3D20")

htmltext = htmlfile.read()

newhtmltext = json.loads(htmltext.replace("{}&&",""))

print newhtmltext["items"]

