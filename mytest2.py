# -*- coding: utf-8 -*-#

from bs4 import BeautifulSoup
import urllib2
import json



temp_url = "http://map.naver.com/search2/local.nhn?query=%EC%B2%AD%EB%8B%B4%EB%8F%99+%EC%8A%A4%EC%8B%9C&page=2"
url = temp_url
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
r = urllib2.Request(url, headers=headers)

htmltext = urllib2.urlopen(r,timeout=10).read()
data = json.loads(htmltext)

for item in data['result']['site']['list'] :
	print item['name'].encode('utf-8');
	print item['roadAddress'].encode('utf-8');
	print item['streetPanorama']['lng'].encode('utf-8');
	print item['streetPanorama']['lat'].encode('utf-8');
