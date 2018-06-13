#!/usr/bin/env python3.5
from bs4 import BeautifulSoup
import requests

'''

'''

def scrape_document(uoc):
    page = requests.get("http://training.gov.au/Training/Details/" + uoc)

    soup = BeautifulSoup(page.content,'html.parser')
    document_title = soup.title.get_text()

    unit_code = uoc
    unit_name = document_title.split('-')[-1].lstrip()
    assess_tool_ver = uoc + "_Assessment_Mapping_Toolv1.1"
    range_statement = ""
    asp_of_evidence = ""
    elem_perf_criteria = []
    req_skill_knowledge = []

    for e in soup.find_all("h2"):
        if e.string == "Range Statement":
            print(e.string)
            range_table = e.find_next_siblings()[0]
            extract_range_statement(range_table)
            
def extract_range_statement(table):
    for table_row in table:
        print(table_row.find("td"))
        print("Done")


uoc_names = ["UEENEEK142A"]
document_title = ''
'''
url = input("Enter Unit of Competency Code e.g. UEENEEK142A: ")
while (url):
    uoc_names.append(url)
    url = input("Enter Unit of Competency Code e.g. UEENEEK142A: ")
'''
for unit in uoc_names:
    scrape_document(unit)
print("Process Complete")
