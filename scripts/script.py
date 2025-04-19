import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import openpyxl

parent_page, child_page = [], []

# use regex to assign which page is going to be scanned next (nav menu info)
# use regex to create a mass downloader

url = input("Enter the department link address ")
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

link_patterns = re.compile(r'sites|StanStatePublicDocs')
relevant_links = soup.find_all(href=link_patterns)

link_name, link_address, migration_status, deletion_status = [], [], [], []

if len(relevant_links) != 0:
    for relevant_link in relevant_links:
        link_name.append(relevant_link.get_text())
        link_address.append(relevant_link.get('href'))
        migration_status.append(' ')
        deletion_status.append(' ')
        parent_page.append(' ') # remove once pagination is set
        child_page.append(' ') # remove once pagination is set
else:
    link_name.append(' ')
    link_address.append(' ')
    migration_status.append(' ')
    deletion_status.append(' ')
    parent_page.append(' ') # remove once pagination is set
    child_page.append(' ') # remove once pagination is set
    print("No links present on this page.")

df = pd.DataFrame(parent_page, columns = ['Parent Page'])
df['Child Page'] = child_page
df['Link Name'] = link_name
df['Link Address'] = link_address
df['Migrated to SP'] = migration_status
df['Deleted off D10'] =  deletion_status

print(df)
df = df.to_excel("Documents.xlsx")

'''
COMPILING COLUMN VALUES (VERSION 2)

parent_page.append(soup.find(class_='nav navbar-nav').text)
parent_page = soup.find(class_='nav navbar-nav').text

child_page = soup.find(class_='dropdown-link').text
child_page.append( ().find('a') )
____________________________________________

ADDING DATA TO DATAFRAME (VERSION 1)

totalLinks = pd.Series(totalLinks, name="Link Addresses")

totalLinks = totalLinks.to_excel("Links.xlsx")
print('The links were documented in the Excel File successfully.')

drupalLinks = pd.Series((drupalLinks), name="Drupal Documents")
sharepointLinks = pd.Series((sharepointLinks), name="SharePoint Documents")

result = (pd.concat([drupalLinks, sharepointLinks], axis=1)).to_excel("Links.xlsx")
'''