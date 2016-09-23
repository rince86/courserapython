import xml.etree.ElementTree as ET

data = '''
<person>
	<name>Slawek</name>
	<phone type="intl">
	+48 666 666 666
	</phone>
	<email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print 'Name:',tree.find('name').text
print 'Attr:',tree.find('email').get('hide')
