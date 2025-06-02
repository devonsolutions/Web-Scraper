import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import openpyxl
import os
from collections.abc import Iterable

departmentURL = input("Enter the department link address ")

requestPage = requests.get(departmentURL)
pageHTML = BeautifulSoup(requestPage.content, "html.parser")

navLinks = pageHTML.find_all(class_="nav-link")

navHREFs = []

for navLink in navLinks:
    navHREFs.append(navLink.get('href'))

parentPages = []

departmentPath = re.split(r'/', departmentURL)
departmentPath = departmentPath.pop(3)
departmentPath = "/" + departmentPath + "/"

for navHREF in navHREFs:
    if type(navHREF) == str:
        if departmentPath in navHREF:
            navHREF = "https://csustan.edu" + navHREF
            parentPages.append(navHREF)
    else:
        pass
    
for parentPage in parentPages:
    print(parentPage)

'''

link_name, link_address, migration_status, deletion_status = [], [], [], []

def store_page():
    global soup
    page = requests.get(department_address)
    soup = BeautifulSoup(page.content, "html.parser")

def compile_links():
    global relevant_links
    link_patterns = re.compile(r'sites|StanStatePublicDocs')
    relevant_links = soup.find_all(href=link_patterns)

def add():
    if relevant_links:
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

store_page()
compile_links()
add()

df = pd.DataFrame(link_name, columns = ['Link Name'])
df['Link Address'] = link_address
df['Migrated to SP'] = migration_status
df['Deleted off D10'] =  deletion_status

excel_name = department_address.replace("https://www.csustan.edu/financial-support-services/procurement-contract-services/", "")

file_path = "/Users/jerynnecenario/Downloads/"
file = os.path.join(file_path, excel_name)

df = df.to_excel(file + ".xlsx")

print("Downloaded: " + str(file))
'''