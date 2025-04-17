import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re

doc_name, doc_link, migration_status, deletion_status = [], [], [], []

url = input("Enter the department link address ")
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

link_patterns = re.compile(r'sites|StanStatePublicDocs')
relevant_links = soup.find_all(href=link_patterns)

if len(relevant_links) != 0:
    for relevant_link in relevant_links:
        doc_link.append(relevant_link.get('href'))
        doc_name.append('')
        # print(relevant_link)
    print(doc_link)
    # print(relevant_links)
    # print("Links PRESENT.")
else:
    print("Links NOT present.")

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
____________________________________________

ADDING DATA TO DATAFRAME (VERSION 2)

df = pd.DataFrame(parent_page, columns = ['Parent Page'])

df['Child Page'], df['Document Name'], = child_page, doc_name
df['Document Link'], df['Migrated to SP'], df['Deleted off D10'], = doc_link, migrated_status, deletion_status
'''