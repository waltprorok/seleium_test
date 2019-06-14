import requests
from bs4 import BeautifulSoup as bs

url = requests.get("https://www.ticketsatwork.com")
soup = bs(url.text, 'html.parser')
links = soup.find_all('a')
count = 0
taw_links = []


for link in links:
    taw_links.append(link.get('href'))
    # count += 1

for taw_link in taw_links:
    print(taw_link)

# print('Count: ' + str(count))
