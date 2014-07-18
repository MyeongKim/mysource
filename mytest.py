# -*- coding: utf-8 -*-#

from bs4 import BeautifulSoup
import urllib2
import json


for i in range(1,500):
	temp_url = "http://map.naver.com/search2/local.nhn?query=%EB%84%A4%EC%9D%BC%EC%95%84%ED%8A%B8&page="
	url = temp_url + str(i)
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

	

