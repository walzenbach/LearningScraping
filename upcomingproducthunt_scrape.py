from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.producthunt.com/upcoming'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# create empty list
product = []
desc = []

items = soup.find_all('div', class_='item_6a520')
for i in items:
    itemName = i.find('div', class_='font_9d927 black_476ed large_db9e7 light_4a7e0 title_39c87 lineHeight_042f1 underline_57d3c').text
    itemDesc = i.find('div', class_='font_9d927 grey_bbe43 small_231df normal_d2e66 tagline_ce810 lineHeight_042f1 underline_57d3c').text
    product.append(itemName)
    desc.append(itemDesc)

# create dataframe from your lists
df = pd.DataFrame(list(zip(product, desc)), 
           columns =['product', 'desc'])

df.to_csv('upcomingproducts.csv', index=False, header=True)

#run terminal command cd ~/Desktop to execute file on desktop