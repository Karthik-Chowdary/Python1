# Install BeautifulSoup :
# pip install BeautifulSoup4
#
# Alternatively you can also do this:
# http://py4e.com/code3/bs4.zip
# Download the file and extract in the file where your code is present

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter the url: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrive all the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
