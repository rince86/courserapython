import urllib
handle = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in handle:
	line = line.strip()
	print line
