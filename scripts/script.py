import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re


URL = "https://www.csustan.edu/financial-support-services/procurement-contract-services/bid-bid-results"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

drupalDocuments = soup.find_all(href=re.compile("/sites"))
print(drupalDocuments)

sharepointDocuments = soup.find_all(href=re.compile("/StanStatePublicDocs"))
print(sharepointDocuments)

# creating the DataFrame
documents = pd.DataFrame({'Cars': ['BMW', 'Audi', 'Bugatti',
                                   'Porsche', 'Volkswagen'],
                          'MaxSpeed': [220, 230, 240, 210, 190],
                          'Color': ['Black', 'Red', 'Blue',
                                    'Violet', 'White']})

# writing to Excel
datatoexcel = pd.ExcelWriter('Documents.xlsx')

# write DataFrame to excel
documents.to_excel(datatoexcel)

# save the excel
datatoexcel.close()
print('DataFrame is written to Excel File successfully.')

# https://stackoverflow.com/questions/34997174/how-to-convert-list-of-model-objects-to-pandas-dataframe
# https://stackoverflow.com/questions/6750240/how-to-do-re-compile-with-a-list-in-python 