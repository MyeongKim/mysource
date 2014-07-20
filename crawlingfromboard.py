import urllib2
from bs4 import BeautifulSoup

# 


for i in range(1,10):
	temp_url = "http://valley.egloos.com/theme/food/page/"
	url = temp_url + str(i)
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	r = urllib2.Request(url, headers=headers)

	htmltext = urllib2.urlopen(r,timeout=10).read()
	soup = BeautifulSoup(htmltext, from_encoding="utf-8")
#
	authors = []

	for tag in soup.select(".popular"):
		authors.append(tag.get_text())

	for author in authors:
		print author.encode('utf-8');


