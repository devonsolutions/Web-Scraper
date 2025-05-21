import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import openpyxl

department_address = input("Enter the department link address ")
page = requests.get(department_address)
soup = BeautifulSoup(page.content, "html.parser")

link_name, link_address, migration_status, deletion_status = [], [], [], []

link_patterns = re.compile(r'sites|StanStatePublicDocs')
relevant_links = soup.find_all(href=link_patterns)

if len(relevant_links) != 0:
    for relevant_link in relevant_links:
        link_name.append(relevant_link.get_text())
        link_address.append(relevant_link.get('href'))
        migration_status.append(' ')
        deletion_status.append(' ')
else:
    link_name.append('No links present on this page.')
    link_address.append(' ')
    migration_status.append(' ')
    deletion_status.append(' ')

df = pd.DataFrame(link_name, columns = ['Link Name'])
df['Link Address'] = link_address
df['Migrated to SP'] = migration_status
df['Deleted off D10'] =  deletion_status

excel_name = department_address.replace("https://www.csustan.edu/financial-support-services/procurement-contract-services/", " ")

df = df.to_excel(excel_name + ".xlsx")


