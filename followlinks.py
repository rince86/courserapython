import urllib
from BeautifulSoup import *

url = raw_input('Enter url: ')
if len(url) < 1:
	url = "http://python-data.dr-chuck.net/known_by_Fikret.html"
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))

print url
while (count != 0):
	pos = 0
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	for tag in tags:
		if pos == (position-1):
			url = tag.get('href', None)
			print url
			count -= 1
			break
		pos += 1
