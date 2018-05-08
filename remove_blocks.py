#!/usr/bin/env python3.5
from bs4 import BeautifulSoup

'''
Removes side blocks and other unecessary features from a moodle page
'''


document_title = ''

#url = input("Enter path: ").replace('\\','\\\\')

url = "C:\\Users\\harri\\Desktop\\Installation Testing.html"
soup = BeautifulSoup(open(url),'html.parser')
document_title = soup.title.get_text()

#removes log out button

#removes submenu
for div in soup.find_all("div", {'class':'lb_submenu'}): 
    div.decompose()

#removes 
html = soup.prettify("utf-8")
output_file = document_title + ' - MODIFIED.html'
with open(output_file, "wb") as file:
    file.write(html)
