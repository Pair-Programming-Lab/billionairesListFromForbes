from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.forbes.com/billionaires/list/#version:static'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
rows = page_soup.findAll(
    'tr',
    {
        'class': 'ad'
    }
)

filename = "bList.csv"
f = open(filename, 'w')
headers = "Rank , Name, Company, Worth\n"
f.write(headers)

print(len(rows))
for row in rows:

    brand = container.div.div.a.img['title']
    title_container = container.findAll('a', {'class': 'item-title'})
    product_name = title_container[0].text

    shipping_container = container.findAll('li', {'class': 'price-ship'})
    shipping = shipping_container[0].text.strip()

    Rank = row.
Name
Company
Worth
    f.write(Rank + ',' + Name + ',' + Company + ',' + Worth + '\n')

f.close()
