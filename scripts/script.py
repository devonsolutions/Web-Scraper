import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import openpyxl
from openpyxl.styles import PatternFill

URL = "https://www.csustan.edu/financial-support-services/procurement-contract-services/bid-bid-results"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# totalLinks = []
# totalNames = []

# drupalLinks = soup.find_all(href=re.compile("/sites"))

#for link in drupalLinks:
    #totalLinks.append(link.get('href'))

for name in soup.find_all('a'):
    txt = name.get('a')
    print(txt)

#sharepointLinks = soup.find_all(href=re.compile("/StanStatePublicDocs"))

#for link in sharepointLinks:
    #totalLinks.append(link.get('href'))

#totalLinks = pd.Series(totalLinks, name="Link Addresses")


#totalLinks = totalLinks.to_excel("Links.xlsx")
#print('The links were documented in the Excel File successfully.')

'''
drupalLinks = pd.Series((drupalLinks), name="Drupal Documents")
sharepointLinks = pd.Series((sharepointLinks), name="SharePoint Documents")

result = (pd.concat([drupalLinks, sharepointLinks], axis=1)).to_excel("Links.xlsx")
'''

# https://stackoverflow.com/questions/34997174/how-to-convert-list-of-model-objects-to-pandas-dataframe
# https://stackoverflow.com/questions/6750240/how-to-do-re-compile-with-a-list-in-python'
# https://stackoverflow.com/questions/18062135/combining-two-series-into-a-dataframe-in-pandas
# https://www.geeksforgeeks.org/how-to-add-colour-to-excel-cells-using-python/
# https://docs.python.org/3/library/unittest.html
# https://www.geeksforgeeks.org/how-to-add-colour-to-excel-cells-using-python/

# Extra Text from Anchor Tag https://stackoverflow.com/questions/11716380/beautifulsoup-extract-text-from-anchor-tag