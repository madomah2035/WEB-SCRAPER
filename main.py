from bs4 import BeautifulSoup
import requests as re

url = "https://jiji.com.gh/mobile-phones?filter_attr_45_brand=Samsung"

response = re.get(url)

soup = BeautifulSoup(response.content, 'lxml')

divs = soup.div
print(divs.prettify())
