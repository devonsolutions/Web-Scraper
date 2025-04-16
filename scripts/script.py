import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re

# VERSION 3: singular page
# To-Do List:
# Evaluate href values as a boolean (add links to list in order)
# Add document name values to list
# Add 

url = input("Enter the department link address ")
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

links = soup.find_all('a')
relevant_links = []

if len(links) != 0:
    for link in links:
        # I want to the scanner to go through each link
        # If the link href contains "/sites" or "/StanStatePublicDocs"
        #   then it gets appended (in the order that the link appears on the page)
        # Else relevant_links.append(None)
        relevant_links.append(soup.find(href=re.compile("/sites")))
        relevant_links.append(soup.find(href=re.compile("/StanStatePublicDocs")))
else:
    relevant_links.append(None)
    # If there are no links on this page, the program should move onto the next page

# All D10 and SharePoint docs are stored in the relevant_links list, in order
print(relevant_links)

# Lists (columns) generated: document name, document, link, migration status, deletion status
doc_name, doc_link, migration_status, deletion_status = [], [], [], []

if len(relevant_links) != 0:
    for relevant_link in relevant_links:
        doc_name.append(None)
        # relevant_links.find('a').text
        doc_link.append(None)
        migration_status.append(None)
        deletion_status.append(None)
else:
    doc_name.append(None)
    doc_link.append(None)
    migration_status.append(None)
    deletion_status.append(None)
    print("There are no D10 or SharePoint documents on this page.")
    # On the Excel sheet, if there are no D10 or SharePoint documents, the program will generate an empty Excel sheet template



'''
VERSION 1

totalLinks = []

drupalLinks = soup.find_all(href=re.compile("/sites"))
for link in drupalLinks:
    totalLinks.append(link.get('href'))

sharepointLinks = soup.find_all(href=re.compile("/StanStatePublicDocs"))
for link in sharepointLinks:
    totalLinks.append(link.get('href'))

totalLinks = pd.Series(totalLinks, name="Link Addresses")

totalLinks = totalLinks.to_excel("Links.xlsx")
print('The links were documented in the Excel File successfully.')


drupalLinks = pd.Series((drupalLinks), name="Drupal Documents")
sharepointLinks = pd.Series((sharepointLinks), name="SharePoint Documents")

result = (pd.concat([drupalLinks, sharepointLinks], axis=1)).to_excel("Links.xlsx")
'''

'''
VERSION 2

doc_name = soup.find(href=re.compile("/StanStatePublicDocs")).text
print(doc_name)

parent_page, child_page, doc_name, doc_link, migrated_status, deletion_status = [], [], [], [], [], []

parent_page.append(soup.find(class_='nav navbar-nav').text)
parent_page = soup.find(class_='nav navbar-nav').text

child_page = soup.find(class_='dropdown-link').text
child_page.append( ().find('a') )

doc_name.append(soup.find('a')
doc_link.append( ().find('a') )
migrated_status.append(None)
deletion_status.append(None)

df = pd.DataFrame(parent_page, columns = ['Parent Page'])

df['Child Page'], df['Document Name'], = child_page, doc_name
df['Document Link'], df['Migrated to SP'], df['Deleted off D10'], = doc_link, migrated_status, deletion_status

# return df
'''