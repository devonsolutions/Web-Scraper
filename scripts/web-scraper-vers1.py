# https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
# https://stackoverflow.com/questions/19429126/scrape-through-website-with-href-references

import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.csustan.edu/financial-support-services/procurement-contract-services/bid-bid-results"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

# tutorial START

quotes=[]  # a list to store quotes
 
table = soup.find('div', attrs = {'id':'all_quotes'}) 
 
for row in table.findAll('div', attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split("")[0]
    quote['author'] = row.img['alt'].split("")[1]
    quotes.append(quote)

# tutorial END

filename = 'inspirational_quotes.csv'
# upgrade: filename should be user input "name"
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,
    ['theme','url','img','lines','author'] )
    w.writerheader()
    for quote in quotes:
        w.writerow(quote)
