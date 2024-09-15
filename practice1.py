from bs4 import BeautifulSoup
# import requests as re

# file = 'example.html'
# file_content = open(file, 'r')
#
# soup = BeautifulSoup(file_content, 'html.parser')
# file_content.close()

with open('example.html', 'r') as source_code:
    soup = BeautifulSoup(source_code, 'lxml')

a_tags = soup.find('a').text

print(a_tags)
