#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys

'''
Removes side blocks and other unecessary features from a moodle page
'''


document_title = ''

print("For example:\tC:\\Users\\harri\\Documents\\GitHub\\NECA\\Installation Testing.html")
original_location = input("Enter path to orignal: ").replace('\\','\\\\')
print("For example:\tC:\\Users\\harri\\Documents\\GitHub\\NECA\\")
modified_location = input("Enter path for modified: ").replace('\\','\\\\')

try:
    soup = BeautifulSoup(open(original_location),'html.parser')
except FileNotFoundError:
    print("\n\nINVALID SOURCE FILE LOCATION\n\n")
    sys.exit()
document_title = soup.title.get_text()

#removes log out button
for div in soup.find_all("div", {"id":"page-header"}): 
    div.decompose()

#removes submenu
for div in soup.find_all("div", {"class":"lb_submenu"}): 
    div.decompose()

#removes side bar
for div in soup.find_all("div", {"id":"block-region-side-pre"}):
    div.decompose()

#remove quiz stats (time, %, etc)

for div in soup.find_all("table", {"class":"quizreviewsummary"}):
    div.decompose()

#removes footer
for div in soup.find_all("div", {"id":"page-footer"}):
    div.decompose()

html = soup.prettify("utf-8")


output_file = modified_location + document_title + " - MODIFIED.html"
try:
    with open(output_file, "wb") as file:
        file.write(html)
except FileNotFoundError:
    print("INVALID FILE OUTPUT LOCATION")
    sys.exit()
