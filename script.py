from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd
import requests
import re
import os
import certifi

UNIVERSITY_PATH = "https://www.csustan.edu"
DEPARTMENT_LINK_ADDRESS = input("Enter the department link address ")
DEPARTMENT_NAME = DEPARTMENT_LINK_ADDRESS.replace("https://www.csustan.edu/", "")

FOLDER_PATH = str(Path.home() / "Downloads") + "/" + DEPARTMENT_NAME

ACCESS_REQUEST = requests.get(DEPARTMENT_LINK_ADDRESS, verify=certifi.where())
PAGE_HTML = BeautifulSoup(ACCESS_REQUEST.content, "html.parser")

navigation_links = PAGE_HTML.find_all(class_="nav-link")

navigation_HREFs = []

for navigation_link in navigation_links:
    navigation_HREFs.append(navigation_link.get('href'))

department_path = re.split(r'/', DEPARTMENT_LINK_ADDRESS)
department_path = department_path.pop(3)
department_path = "/" + department_path + "/"

parent_pages = []

for navigation_HREF in navigation_HREFs:
    if (type(navigation_HREF) == str) and (UNIVERSITY_PATH and department_path in navigation_HREF):
        navigation_HREF = UNIVERSITY_PATH + navigation_HREF
        parent_pages.append(navigation_HREF)
        print(navigation_HREF)
    else:
        pass


department_pages = []

for parent_page in parent_pages:
    department_pages.append(parent_page)
    parent_page_request = requests.get(parent_page, verify=certifi.where())
    page_html = BeautifulSoup(parent_page_request.content, "html.parser")

    dropdown_items = page_html.find_all(class_="dropdown-item")

    for dropdown_item in dropdown_items:
        dropdown_item_links = dropdown_item.find_all("a")
        child_page_HREFs = []

        for dropdown_item_link in dropdown_item_links:
            child_page_HREFs.append(dropdown_item_link.get('href'))

        for child_page_HREF in child_page_HREFs:
            if type(child_page_HREF) == str:
                if department_path in child_page_HREF:
                    department_path = UNIVERSITY_PATH + child_page_HREF
                    department_pages.append(child_page_HREF)
                    print(child_page_HREF)
                else:
                    pass

page_name, page_link, document_name, document_link, migration_status, deletion_status = [], [], [], [], [], []

for department_page in department_pages:
    page = requests.get(department_page)
    soup = BeautifulSoup(page.content, "html.parser")

    LINK_PATTERNS = re.compile(r'sites|sharepoint|pdf|drive|doc')
    relevant_links = soup.find_all(href=LINK_PATTERNS)

    if relevant_links:
        for relevant_link in relevant_links:
            page_name.append(soup.find('h1', class_= 'title'))
            page_link.append(department_page)
            document_name.append(relevant_link.get_text())
            document_link.append(relevant_link.get('href'))

            # .append('') is necessary for the list to be translated into a dataframe column
            migration_status.append('')
            deletion_status.append('')

    else:
        page_name.append(soup.find('h1', class_= 'title'))
        page_link.append(department_page)
        document_name.append('No links present on this page.')
        document_link.append('')
        migration_status.append('')
        deletion_status.append('')

data_frame = pd.DataFrame(page_name, columns = ['Page Name'])
data_frame['Page Link'] = page_link
data_frame['Document Name'] = document_name
data_frame['Document Link'] = document_link
data_frame['Migrated to SP'] = migration_status
data_frame['Deleted off D10'] =  deletion_status

hyper_links = []

for page_name,page_link in zip(data_frame['Page Name'], data_frame['Page Link']):
    hyper_links.append(f'=HYPERLINK("{page_link}", "{page_name}") \n')

data_frame['Page Name'] = hyper_links

if not os.path.exists(FOLDER_PATH):
    os.makedirs(FOLDER_PATH)

file_path = os.path.join(FOLDER_PATH, DEPARTMENT_NAME)

data_frame = data_frame.drop('Page Link', axis=1)
data_frame = data_frame.to_excel(file_path + ".xlsx")

print("Downloaded: " + str(file_path))
