import xml.etree.ElementTree as ET
import codecs
#from codecs import open

#tree = ET.parse('c:/tmp/country_data.xml')
with codecs.open('c:/tmp/country_data.xml', 'r') as xml_file:
    tree = ET.parse(xml_file)
#root = ET.fromstring(country_data)

root = tree.getroot()

print '\n0.'
print root.tag, root.attrib, root[1][1].text

print '\n1.'
for child in root:
    print child.tag, child.attrib

print '\n2.'
for neighbor in root.iter('neighbor'):
    print neighbor.attrib

print '\n3.'
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print name, rank

