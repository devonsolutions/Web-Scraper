import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import certifi
import openpyxl

departmentLinkAddress = input("Enter the department link address ")

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

pageName, linkName, linkAddress, migrationStatus, deletionStatus = [], [], [], [], []

for departmentPage in departmentPages:
    page = requests.get(departmentPage)
    soup = BeautifulSoup(page.content, "html.parser")

    linkPatterns = re.compile(r'sites|sharepoint|pdf|drive|doc')
    relevantLinks = soup.find_all(href=linkPatterns)

    if relevantLinks:
        for relevantLink in relevantLinks:
            pageName.append(departmentPage)
            linkName.append(relevantLink.get_text())
            linkAddress.append(relevantLink.get('href'))
    else:
        pageName.append(departmentPage)
        linkName.append('No links present on this page.')

dataFrame = pd.DataFrame(pageName, columns = ['Page Name'])
dataFrame['Link Name'] = linkName
dataFrame['Link Address'] = linkAddress
dataFrame['Migrated to SP'] = migrationStatus
dataFrame['Deleted off D10'] =  deletionStatus

departmentName = departmentLinkAddress.replace("https://www.csustan.edu/", "")

filePath = "/Users/jerynnecenario/Downloads/"
fileName = os.path.join(filePath, departmentName)

dataFrame = dataFrame.to_excel(fileName + ".xlsx")

print("Downloaded: " + str(fileName))