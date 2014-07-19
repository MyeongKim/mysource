#-*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup
import smtplib
import time

htmltext = urllib.urlopen("http://likelion.fiv3star.me/index.php?mid=board_MzBS61").read()

soup = BeautifulSoup(htmltext, from_encoding="utf-8")

authors = []

# assignment one.

for tag in soup.select("td.title"):
	authors.append(tag.get_text())


for author in authors:
	print author.encode('utf-8')




# assignment two.

# while True :

# 	htmltext = urllib.urlopen("http://likelion.fiv3star.me/index.php?mid=board_MzBS61").read()

# 	soup = BeautifulSoup(htmltext, from_encoding="utf-8")

# 	mylists = []

# 	for tag in soup.select("td.title"):
# 		mylists.append(tag.get_text())
		
# 	if mylists[0] not in authors:

# 		print mylists[0].encode('utf-8')
# 		authors.append(mylists[0])
# 		time.sleep(5)

# aaa..............sad



# assignment three


# Specifying the from and to addresses

# Writing the message (this message will appear in the email)



while True :

	htmltext = urllib.urlopen("http://likelion.fiv3star.me/index.php?mid=board_MzBS61").read()

	soup = BeautifulSoup(htmltext, from_encoding="utf-8")

	mylists = []
	keywords = ['cheese','window','apple']

	for tag in soup.select("td.title"):
		mylists.append(tag.get_text())

	if mylists[0] not in authors:

		print mylists[0].encode('utf-8')
		authors.append(mylists[0])
		str1 = ''.join(mylists)

		if any(word in str1 for word in keywords):

			fromaddr = 'ming3772@gmail.com'
			toaddrs  = 'ming3772@gmail.com'

			msg = 'new thing is : \n' + mylists[0]

			# Gmail Login

			username = 'ming3772@gmail.com'
			password = 'I\'llgotoyou'

			# Sending the mail  

			server = smtplib.SMTP('smtp.gmail.com:587')
			server.starttls()
			server.login(username,password)
			server.sendmail(fromaddr, toaddrs, msg)
			server.quit()

	time.sleep(5)