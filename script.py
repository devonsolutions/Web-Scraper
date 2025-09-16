from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd
import requests
import re
import os
import certifi
import openpyxl

'''
UNIVERSITY_LINK_ADDRESS = "https://www.csustan.edu"
DEPARTMENT_LINK_ADDRESS = input("Enter the department link address ")
DEPARTMENT_NAME = DEPARTMENT_LINK_ADDRESS.replace("https://www.csustan.edu", "")
DEPARTMENT_PATH = DEPARTMENT_NAME + "/"

FOLDER_PATH = str(Path.home() / "Downloads") + DEPARTMENT_NAME 
FILE_PATH = os.path.join(FOLDER_PATH + DEPARTMENT_NAME)

DOCUMENT_LINK_PATTERNS = re.compile(r'sites|sharepoint|pdf|drive|doc')

page_name, document_name, document_link, migration_status, deletion_status = [], [], [], [], []

navigation_HREFs, child_page_HREFs = [], []
pages, child_pages = [], []

def collect_home_page_html():
    global home_page_access_request
    global home_page_html
    home_page_access_request = requests.get(DEPARTMENT_LINK_ADDRESS, verify=certifi.where())
    home_page_html = BeautifulSoup(home_page_access_request.content, "html.parser")
    pages.append(DEPARTMENT_LINK_ADDRESS)

def identify_navigation_HREF_values():
    navigation_links = home_page_html.find_all(class_="nav-link")
    for navigation_link in navigation_links:
        navigation_HREFs.append(navigation_link.get('href'))

def collect_parent_pages():
    for navigation_HREF in navigation_HREFs:
        if type(navigation_HREF) == str and (UNIVERSITY_LINK_ADDRESS and DEPARTMENT_PATH in navigation_HREF):
            navigation_HREF = UNIVERSITY_LINK_ADDRESS + navigation_HREF
            pages.append(navigation_HREF)
        else:
            pass

# Since the ".find_all" method produces a list, nested For Loops are necessary for filtering through the each instance of a dropdown-item.
# To resolve the issue of a duplicates, a function has been added below to remove duplicates.

def collect_child_pages():

    dropdown_items = parent_page_html.find_all(class_="dropdown-item")

    for dropdown_item in dropdown_items:
        dropdown_item_links = dropdown_item.find_all("a")

        for dropdown_item_link in dropdown_item_links:
            child_page_HREFs.append(dropdown_item_link.get('href'))

        for child_page_HREF in child_page_HREFs:
            if (type(child_page_HREF) == str) and (DEPARTMENT_PATH in child_page_HREF):
                child_page_HREF = UNIVERSITY_LINK_ADDRESS + child_page_HREF
                child_pages.append(child_page_HREF)
            else:
                pass

def collect_parent_page_html():
    for page in pages:
        global parent_page_access_request
        global parent_page_html
        parent_page_access_request = requests.get(page, verify=certifi.where())
        parent_page_html = BeautifulSoup(parent_page_access_request.content, "html.parser")

        collect_child_pages()

def remove_duplicates_from_child_pages():
    for child_page in child_pages:
        if child_page not in pages:
            pages.append(child_page)
        else:
            pass

def scan_each_page_for_relevant_links():
    for page in pages:
        page_access_request = requests.get(page)
        page_html = BeautifulSoup(parent_page_access_request.content, "html.parser")

        DOCUMENT_LINK_PATTERNS = re.compile(r'sites|sharepoint|pdf|drive|doc')
        relevant_links = page_html.find_all(href=DOCUMENT_LINK_PATTERNS)
        print(page)
        print(relevant_links)
        
        if relevant_links:
            for relevant_link in relevant_links:
                page_name.append(page_html.find('h1', class_= 'title'))
                document_name.append(relevant_link.get_text())
                document_link.append(relevant_link.get('href'))

                # .append('') is necessary for the list to be translated into a dataframe column
                migration_status.append('')
                deletion_status.append('')

        else:
            page_name.append(page_html.find('h1', class_= 'title'))
            document_name.append('No links present on this page.')
            document_link.append('')
            migration_status.append('')
            deletion_status.append('')
        

FOLDER_PATH = str(Path.home() / "Downloads") + DEPARTMENT_NAME 
FILE_PATH = os.path.join(FOLDER_PATH + DEPARTMENT_NAME)

def create_folder_path():
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH) 
    else:
        print("folder path exists")

def assign_columns_to_data_frame():
    data_frame = pd.DataFrame(page_name, columns = ['Page Name'])
    data_frame['Document Name'] = document_name
    data_frame['Document Link'] = document_link
    data_frame['Migrated to SP'] = migration_status
    data_frame['Deleted off D10'] =  deletion_status

    data_frame = data_frame.to_excel(FILE_PATH + ".xlsx")
    print("Downloaded: " + str(FILE_PATH + ".xlsx"))


collect_home_page_html()
identify_navigation_HREF_values()
collect_parent_pages()
collect_parent_page_html()
remove_duplicates_from_child_pages()
scan_each_page_for_relevant_links()
#create_folder_path()
#assign_columns_to_data_frame()

#print(FILE_PATH)

'''

UNIVERSITY_LINK_ADDRESS = "https://www.csustan.edu"
DEPARTMENT_LINK_ADDRESS = input("Enter the department link address ")
DEPARTMENT_NAME = DEPARTMENT_LINK_ADDRESS.replace("https://www.csustan.edu", "")

FOLDER_PATH = str(Path.home() / "Downloads") + DEPARTMENT_NAME 
FILE_PATH = os.path.join(FOLDER_PATH + DEPARTMENT_NAME)

DEPARTMENT_PATH = DEPARTMENT_NAME + "/"

page_name, document_name, document_link, migration_status, deletion_status = [], [], [], [], []
child_page_HREFs, navigation_HREFs = [], []
department_pages, parent_pages = [], []

def collect_home_page_html():
    global access_request
    global page_html
    access_request = requests.get(DEPARTMENT_LINK_ADDRESS, verify=certifi.where())
    page_html = BeautifulSoup(access_request.content, "html.parser")

navigation_links = page_html.find_all(class_="nav-link")

def add_navigation_HREF_values_to_list():
    for navigation_link in navigation_links:
        navigation_HREFs.append(navigation_link.get('href'))

def add_parent_pages_to_list():
    for navigation_HREF in navigation_HREFs:
        if (type(navigation_HREF) == str) and (UNIVERSITY_LINK_ADDRESS and DEPARTMENT_PATH in navigation_HREF):
            navigation_HREF = UNIVERSITY_LINK_ADDRESS + navigation_HREF
            parent_pages.append(navigation_HREF)
            print(navigation_HREF)
        else:
            pass

def compile_child_pages():
    for parent_page in parent_pages:
        department_pages.append(parent_page)
        parent_page_request = requests.get(parent_page, verify=certifi.where())
        page_html = BeautifulSoup(parent_page_request.content, "html.parser")

        dropdown_items = page_html.find_all(class_="dropdown-item")

        for dropdown_item in dropdown_items:
            dropdown_item_links = dropdown_item.find_all("a")

            for dropdown_item_link in dropdown_item_links:
                child_page_HREFs.append(dropdown_item_link.get('href'))

            for child_page_HREF in child_page_HREFs:
                if (type(child_page_HREF) == str) and (DEPARTMENT_PATH in child_page_HREF):
                    child_page_HREF = UNIVERSITY_LINK_ADDRESS + child_page_HREF
                    department_pages.append(child_page_HREF)
                    print(child_page_HREF)
                else:
                    pass

def assign_link_info_to_lists():
    for department_page in department_pages:
        page = requests.get(department_page)
        soup = BeautifulSoup(page.content, "html.parser")

        LINK_PATTERNS = re.compile(r'sites|sharepoint|pdf|drive|doc')
        relevant_links = soup.find_all(href=LINK_PATTERNS)

        if relevant_links:
            for relevant_link in relevant_links:
                page_name.append(soup.find('h1', class_= 'title'))
                document_name.append(relevant_link.get_text())
                document_link.append(relevant_link.get('href'))

                # .append('') is necessary for the list to be translated into a dataframe column
                migration_status.append('')
                deletion_status.append('')

        else:
            page_name.append(soup.find('h1', class_= 'title'))
            document_name.append('No links present on this page.')
            document_link.append('')
            migration_status.append('')
            deletion_status.append('')

def create_folder_path():
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH) 
    else:
        print("folder path exists")

def save_data_frame_to_excel():
    global data_frame
    data_frame = pd.DataFrame(page_name, columns = ['Page Name'])
    data_frame['Document Name'] = document_name
    data_frame['Document Link'] = document_link
    data_frame['Migrated to SP'] = migration_status
    data_frame['Deleted off D10'] =  deletion_status

    data_frame = data_frame.to_excel(FILE_PATH + ".xlsx")
    print("Downloaded: " + str(FILE_PATH) + ".xlsx")

collect_home_page_html()
add_navigation_HREF_values_to_list()
add_parent_pages_to_list()
compile_child_pages()
assign_link_info_to_lists()
create_folder_path()
save_data_frame_to_excel()