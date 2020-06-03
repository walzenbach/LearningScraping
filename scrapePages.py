from bs4 import BeautifulSoup
import requests
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
for i in items:
    itemName = i.find('h4', class_='card-title').text
    itemPrice = i.find('h5').text
    print(itemName)
    print(itemPrice)
