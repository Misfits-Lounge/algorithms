from urllib import request
from xml.etree import cElementTree as et



url_xml_data = 'http://data.gov.ro/storage/f/2014-12-17T12%3A15%3A13.009Z/mers-tren-sntfc-2014-2015.xml'


def parse_data(url=''):
    tree = et.parse('data.xml')
    root = tree.getroot()

    item = [i for i in tree.getroot()]
    for x in item:
        print(x.tag)
        
parse_data(url_xml_data)
