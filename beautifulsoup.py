import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup('span')
sum = 0
for tag in tags:
	var = int(tag.contents[0])
	sum += var
print sum

# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
    # Look at the parts of a tag
#    print 'TAG:',tag
#    print 'URL:',tag.get('href', None)
#    print 'Contents:',tag.contents[0]
#    print 'Attrs:',tag.attrs
