#!/user/bin/env python

# Print the links to standard out.

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"))

for link in soup.find_all('a'):
    print(link.get('href'))
