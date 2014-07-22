from flask import render_template, Flask, request
app = Flask(__name__)

from apps import app
import urllib2
from bs4 import BeautifulSoup


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])

def index():


	# number one
	# get = None
	# post = None
	
	# if request.args:
	# 	get = request.args['text_get']

	# if request.form:
	# 	post = request.form['text_post']

	# //number one	

	# number two


	url = "http://foodnara.go.kr/kisna/index.do?nMenuCode=17&page=2&mPart=&code2=&code4=2&search_name=&processed=&order_column=2&order_asc=asc"
	f = urllib2.urlopen(url)
	page = f.read().decode('cp949', 'ignore')
	f.close()

	soup = BeautifulSoup(page)
	a = soup.select('.tableGray > tbody > tr')


	# this is just example...
	# print a
	b=a[2].get_text()
	c=b.split('\n')
	c=c[4].encode("utf-8")
	# this is just example...haha


	# get index above me
	# print a
	b=a[2].get_text()
	c=b.split('\n')



	return c