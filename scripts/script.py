from IPython.display import HTML
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import certifi

departmentLinkAddress = input("Enter the department link address ")
departmentName = departmentLinkAddress.replace("https://www.csustan.edu/", "")
folderPath = input("What is your Downloads folder path?") + departmentName

accessRequest = requests.get(departmentLinkAddress, verify=certifi.where())
pageHTML = BeautifulSoup(accessRequest.content, "html.parser")

navigationLinks = pageHTML.find_all(class_="nav-link")

navigationHREFs = []

for navigationLink in navigationLinks:
    navigationHREFs.append(navigationLink.get('href'))

departmentPath = re.split(r'/', departmentLinkAddress)
departmentPath = departmentPath.pop(3)
departmentPath = "/" + departmentPath + "/"

universityPath = "https://www.csustan.edu"

parentPages = []

for navigationHREF in navigationHREFs:
    if type(navigationHREF) == str:
        if departmentPath in navigationHREF:
            if universityPath in navigationHREF:
                pass
            else:
                navigationHREF = universityPath + navigationHREF
                parentPages.append(navigationHREF)
                print(navigationHREF)
        else:
            pass
    else:
        pass

departmentPages = []

for parentPage in parentPages:
    departmentPages.append(parentPage)
    parentPageRequest = requests.get(parentPage, verify=certifi.where())
    pageHTML = BeautifulSoup(parentPageRequest.content, "html.parser")

    dropdownItems = pageHTML.find_all(class_="dropdown-item")

    for dropdownItem in dropdownItems:
        dropdownItemLinks = dropdownItem.find_all("a")
        childPageHREFs = []

        for dropdownItemLink in dropdownItemLinks:
            childPageHREFs.append(dropdownItemLink.get('href'))

        for childPageHREF in childPageHREFs:
            if type(childPageHREF) == str:
                if departmentPath in childPageHREF:
                    childPageHREF = universityPath + childPageHREF
                    departmentPages.append(childPageHREF)
                    print(childPageHREF)
                else:
                    pass

pageName, pageLink, docName, docLink, migrationStatus, deletionStatus = [], [], [], [], [], []

for departmentPage in departmentPages:
    page = requests.get(departmentPage)
    soup = BeautifulSoup(page.content, "html.parser")

    linkPatterns = re.compile(r'sites|sharepoint|pdf|drive|doc')
    relevantLinks = soup.find_all(href=linkPatterns)

    if relevantLinks:
        for relevantLink in relevantLinks:
            pageName.append(soup.find('h1', class_= 'title'))
            pageLink.append(departmentPage)
            docName.append(relevantLink.get_text())
            docLink.append(relevantLink.get('href'))

            # .append('') is necessary for the list to be translated into a dataframe column
            migrationStatus.append('')
            deletionStatus.append('')

    else:
        pageName.append(soup.find('h1', class_= 'title'))
        pageLink.append(departmentPage)
        docName.append('No links present on this page.')
        migrationStatus.append('')
        deletionStatus.append('')

dataFrame = pd.DataFrame(pageName, columns = ['Page Name'])
dataFrame['Page Link'] = pageLink
dataFrame['Document Name'] = docName
dataFrame['Document Link'] = docLink
dataFrame['Migrated to SP'] = migrationStatus
dataFrame['Deleted off D10'] =  deletionStatus

hyperlinks = []

for pageName,pageLink in zip(dataFrame['Page Name'], dataFrame['Page Link']):
    hyperlinks.append(f'=HYPERLINK("{pageLink}", "{pageName}") \n')

dataFrame['Page Name'] = hyperlinks

if not os.path.exists(folderPath):
    os.makedirs(folderPath)

filePath = os.path.join(folderPath, departmentName)

dataFrame = dataFrame.drop('Page Link', axis=1)
dataFrame = dataFrame.to_excel(filePath + ".xlsx")

print("Downloaded: " + str(filePath))
