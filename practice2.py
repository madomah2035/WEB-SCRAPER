from bs4 import BeautifulSoup
import re

with open('san_diego_weather.html', 'r') as file_content:
    soup = BeautifulSoup(file_content, 'html.parser')

try:
    date_tag = soup.find(string="Thursday, January 1, 2015").parent
    print(date_tag)

    days_nav = soup.find_all(text=re.compile("Previous Day | Next Day"))
    # [print(day.parent) for day in days_nav]
    if days_nav:
        print("Tags Found: ", days_nav)
    else:
        print("These Tags Do Not Exist!")



except AttributeError:
    print("Error: Date Not Found!")
