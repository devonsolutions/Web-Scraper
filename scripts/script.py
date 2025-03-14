import requests
from bs4 import BeautifulSoup
import re

URL = "https://www.csustan.edu/financial-support-services/procurement-contract-services/bid-bid-results"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

drupalDocuments = soup.find_all(href=re.compile("/sites"))
print(drupalDocuments)

sharepointDocuments = print(soup.find_all(href=re.compile("/StanStatePublicDocs")))
print(sharepointDocuments)