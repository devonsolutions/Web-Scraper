import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import openpyxl

department_address = input("Enter the department link address ")
page = requests.get(department_address)
soup = BeautifulSoup(page.content, "html.parser")

parent_pages = []
# child_pages = []
link_name, link_address, migration_status, deletion_status = [], [], [], []

def findNavLinks():
    href_pattern = "https://csustan.edu"
    newhrefpattern = department_address.slice(href_pattern)
    print(newhrefpattern)
    #navBar_pattern = re.compile(href_pattern)
    #navBar_links = soup.find_all(href=navBar_pattern) 
    #print(navBar_links) 
'''
    for navBar_link in navBar_links:
        navBar_link = navBar_link.get('href')
        navBar_link = "https://www.csustan.edu" + navBar_link
        parent_pages.append(navBar_link)
def addColumnValues():
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
        print("No links present on this page.")

def createDataFrame():
    df = pd.DataFrame(parent_pages, columns = ['Parent Pages'])
    # df['Child Pages'] = child_pages
    df['Link Name'] = link_name
    df['Link Address'] = link_address
    df['Migrated to SP'] = migration_status
    df['Deleted off D10'] =  deletion_status

    excel_html = soup.find(class_="block-title text-link-black display-2")
    excel_name = excel_html.get_text()

    df = df.to_excel(excel_name + ".xlsx")
    '''

findNavLinks()

#for parent_page in parent_pages:
    #addColumnValues()

#createDataFrame()