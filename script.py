from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd
import requests
import re
import os
import certifi
import openpyxl

UNIVERSITY_LINK_ADDRESS = "https://www.csustan.edu"
DEPARTMENT_LINK_ADDRESS = input("Enter the department link address ")
DEPARTMENT_NAME = DEPARTMENT_LINK_ADDRESS.replace("https://www.csustan.edu", "")
DEPARTMENT_PATH = DEPARTMENT_NAME + "/"

FOLDER_PATH = str(Path.home() / "Downloads") + "/" + DEPARTMENT_NAME
FILE_PATH = os.path.join(FOLDER_PATH, DEPARTMENT_NAME)

relevant_links = []

page_name = []
page_link = []
document_name = []
document_link = []
migration_status = []
deletion_status = []

navigation_HREFs = []

pages = []

def collect_home_page_html():
    global home_page_access_request
    global home_page_html
    home_page_access_request = requests.get(DEPARTMENT_LINK_ADDRESS, verify=certifi.where())
    home_page_html = BeautifulSoup(home_page_access_request.content, "html.parser")
    pages.append(DEPARTMENT_LINK_ADDRESS)

collect_home_page_html()

def identify_navigation_HREF_values():
    navigation_links = home_page_html.find_all(class_="nav-link")
    for navigation_link in navigation_links:
        navigation_HREFs.append(navigation_link.get('href'))

identify_navigation_HREF_values()

def collect_parent_pages():
    for navigation_HREF in navigation_HREFs:
        if type(navigation_HREF) == str and (UNIVERSITY_LINK_ADDRESS and DEPARTMENT_PATH in navigation_HREF):
            navigation_HREF = UNIVERSITY_LINK_ADDRESS + navigation_HREF
            pages.append(navigation_HREF)
        else:
            pass

collect_parent_pages()


print(pages)


'''
def child_page():
    # if child page, add to list pages

child_page()

def collect_relevant_links():
    # define a relevant link
    # collect relevant links
    # add to list

def collect_link_info():
    # take info from relevant_links 
    # add to lists

collect_relevant_links()
collect_link_info()

def assign_lists_to_data_frame():
    # assign lists to data frame

assign_lists_to_data_frame()

def create_folder_path():
    # create a folder path

create_folder_path()

def save_data_frame_to_excel():
    # save data frame to excel

save_data_frame_to_excel()

'''
'''

access_request = requests.get(DEPARTMENT_LINK_ADDRESS, verify=certifi.where())
page_html = BeautifulSoup(access_request.content, "html.parser")

navigation_HREFs = []
navigation_links = page_html.find_all(class_="nav-link")

def add_navigation_HREF_values_to_list():
    for navigation_link in navigation_links:
        navigation_HREFs.append(navigation_link.get('href'))

add_navigation_HREF_values_to_list()

parent_pages = []

def add_parent_pages_to_list():
    for navigation_HREF in navigation_HREFs:
        if (type(navigation_HREF) == str) and (UNIVERSITY_LINK_ADDRESS and DEPARTMENT_PATH in navigation_HREF):
            navigation_HREF = UNIVERSITY_LINK_ADDRESS + navigation_HREF
            parent_pages.append(navigation_HREF)
            print(navigation_HREF)
        else:
            pass

add_parent_pages_to_list()

child_page_HREFs = []
department_pages = []

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

compile_child_pages()

page_name = []
document_name = []
document_link = []
migration_status = []
deletion_status = []

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

assign_link_info_to_lists()

def assign_columns_to_data_frame():
    global data_frame
    data_frame = pd.DataFrame(page_name, columns = ['Page Name'])
    data_frame['Document Name'] = document_name
    data_frame['Document Link'] = document_link
    data_frame['Migrated to SP'] = migration_status
    data_frame['Deleted off D10'] =  deletion_status

assign_columns_to_data_frame() 

def create_folder_path():
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH) 
    else:
        print("folder path exists")

create_folder_path()

def save_data_frame_to_excel():
    data_frame = data_frame.to_excel(FILE_PATH + ".xlsx")
    print("Downloaded: " + str(FILE_PATH))

save_data_frame_to_excel()

'''
