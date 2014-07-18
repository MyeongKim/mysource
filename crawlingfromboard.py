import urllib
from bs4 import BeautifulSoup

htmltext = urllib.urlopen("http://valley.egloos.com/theme/food").read()

soup = BeautifulSoup(htmltext, from_encoding="utf-8")

authors = []

for tag in soup.select(".popular"):
	authors.append(tag.a.get_text())


for tag in soup.select("dl"):
	authors.append(tag.a.get_text())

for author in authors:
	print author.encode('utf-8')