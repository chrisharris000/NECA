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
    elem_perf_criteria = ""
    req_skill_knowledge = ""

    for e in soup.find_all("h2"):
        if e.string == "Range Statement":
            range_table = e.find_next_siblings()[0]
            range_statement = extract_table_data(range_table)

        if e.string == "Evidence Guide":
            evidence_guide_table = e.find_next_siblings()[4]
            asp_of_evidence = extract_table_data(evidence_guide_table)

        if e.string == "Elements and Performance Criteria":
            perf_criteria_table = e.find_next_siblings()[0]
            data = (perf_criteria_table.find_all("tr"))
            for i in range(len(data)):
                elem_perf_criteria += data[i].get_text()

        if e.string == "Required Skills and Knowledge":
            k_and_s_table = e.find_next_siblings()[0]
            data = (k_and_s_table.find_all("tr"))
            for i in range(len(data)):
                req_skill_knowledge += data[i].get_text()
    print(req_skill_knowledge)


def extract_table_data(table):
    s = ''
    for row in table.find_all("td"):
        s += row.get_text()
    return s

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
