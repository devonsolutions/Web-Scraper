import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import openpyxl
import os
from collections.abc import Iterable
import certifi

departmentURL = input("Enter the department link address ")

requestPage = requests.get(departmentURL, verify=certifi.where())
pageHTML = BeautifulSoup(requestPage.content, "html.parser")

navLinks = pageHTML.find_all(class_="nav-link")

navHREFs = []

for navLink in navLinks:
    navHREFs.append(navLink.get('href'))

parentPages = []

departmentPath = re.split(r'/', departmentURL)
departmentPath = departmentPath.pop(3)
departmentPath = "/" + departmentPath + "/"

csustanPath = "https://www.csustan.edu"

for navHREF in navHREFs:
    if type(navHREF) == str:
        if departmentPath in navHREF:
            if csustanPath in navHREF:
                pass
            else:
                navHREF = csustanPath + navHREF
                parentPages.append(navHREF)
                print(navHREF)
        else:
            pass
    else:
        pass

allLinks = []

for parentPage in parentPages:
    print(parentPage)
    allLinks.append(parentPage)
    requestParentPage = requests.get(parentPage, verify=certifi.where())
    pageHTML = BeautifulSoup(requestParentPage.content, "html.parser")

    dropdownITEMS = pageHTML.find_all(class_="dropdown-item")

    for dropdownITEM in dropdownITEMS:
        print(dropdownITEM)
        dropdownITEM_Links = dropdownITEM.find_all("a")
        childHREFS = []

        for dropdownITEM_Link in dropdownITEM_Links:
            childHREFS.append(dropdownITEM_Link.get('href'))

        for childHREF in childHREFS:
            print(childHREF)
            if type(childHREF) == str:
                if departmentPath in childHREF:
                    childHREF = csustanPath + childHREF
                    allLinks.append(childHREF)
                    print(childHREF)
                else:
                    pass

page_name, link_name, link_address, migration_status, deletion_status = [], [], [], [], []

for allLink in allLinks:
    page = requests.get(allLink)
    soup = BeautifulSoup(page.content, "html.parser")

    link_patterns = re.compile(r'sites|sharepoint|pdf')
    relevant_links = soup.find_all(href=link_patterns)

    if relevant_links:
        for relevant_link in relevant_links:
            page_name.append(allLink)
            link_name.append(relevant_link.get_text())
            link_address.append(relevant_link.get('href'))
            migration_status.append(' ')
            deletion_status.append(' ')
    else:
        page_name.append(allLink)
        link_name.append('No links present on this page.')
        link_address.append(' ')
        migration_status.append(' ')
        deletion_status.append(' ')

df = pd.DataFrame(page_name, columns = ['Page Name'])
df['Link Name'] = link_name
df['Link Address'] = link_address
df['Migrated to SP'] = migration_status
df['Deleted off D10'] =  deletion_status

excel_name = departmentURL.replace("https://www.csustan.edu/", "")

file_path = "/Users/jerynnecenario/Downloads/"
file = os.path.join(file_path, excel_name)

df = df.to_excel(file + ".xlsx")

print("Downloaded: " + str(file))