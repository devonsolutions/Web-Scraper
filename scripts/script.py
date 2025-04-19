import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import openpyxl

# use regex to assign which page is going to be scanned next (nav menu info)
# use regex to create a mass downloader

department_address = input("Enter the department link address ")
page = requests.get(department_address)
soup = BeautifulSoup(page.content, "html.parser")

parent_pattern = re.compile(r'___')
child_pattern = re.compile(r'____')

link_patterns = re.compile(r'sites|StanStatePublicDocs')
relevant_links = soup.find_all(href=link_patterns)

parent_pages, child_pages = [], []

link_name, link_address, migration_status, deletion_status = [], [], [], []

if len(relevant_links) != 0:
    for relevant_link in relevant_links:
        link_name.append(relevant_link.get_text())
        link_address.append(relevant_link.get('href'))
        migration_status.append(' ')
        deletion_status.append(' ')
        parent_pages.append(' ') # remove once pagination is set
        child_pages.append(' ') # remove once pagination is set
else:
    link_name.append('No links present on this page.')
    link_address.append(' ')
    migration_status.append(' ')
    deletion_status.append(' ')
    parent_pages.append(' ') # remove once pagination is set
    child_pages.append(' ') # remove once pagination is set
    print("No links present on this page.")

df = pd.DataFrame(parent_pages, columns = ['Parent Pages'])
df['Child Pages'] = child_pages
df['Link Name'] = link_name
df['Link Address'] = link_address
df['Migrated to SP'] = migration_status
df['Deleted off D10'] =  deletion_status

df = df.to_excel("Documents.xlsx")

# excel sheet should save to downloads (research python library os)
# Add colors to top row
# Set up column width auto-fit