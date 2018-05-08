#!/usr/bin/env python3.5
from bs4 import BeautifulSoup


'''
Program which scrapes questions, answers and feedback from local html file

Currently (26/04/18), questions with drop downs as answers cannot have its answer
scraped, in addition to questions that have drag and drop features.

Therefore, numbering of questions, answers and feedback will not necessarily match

Another 'bug' is that this character (Â) appears sometimes, and without
looking too indepth, it's just easier to not worry about them unless necessary

Thoughts for improvement:
first look at question type (e.g. multichoice, truefalse) , so that it can be stored and empty spaces can be
inserted if a question is not scrapable.
'''


questions = []
answers = []
feedback = []
document_title = ''

url = input("Enter path: ").replace('\\','\\\\')
soup = BeautifulSoup(open(url),'html.parser')
document_title = soup.title.get_text()

for content_div in soup.find_all('div',class_='content'):

    #scrapes question
    for q_div in content_div.find_all('div',class_='qtext'):
        q = q_div.get_text()
        questions.append(q)

    #scrapes answer
    for answer_div in content_div.find_all('div',class_='correct'):
        a = answer_div.get_text()
        answers.append(a)

    #scrapes feedback
    for feedback_div in content_div.find_all('div',class_='rightanswer'):
        suggested = feedback_div.get_text()
        feedback.append(suggested)
    
output_format = input("Print in shell or output to file (S/F): ")

if output_format == 'S':
    print("Disclaimer: running program in shell will likely cause an error")
    print("Document: {}".format(document_title))

    print("QUESTIONS")
    for index, question in enumerate(questions):
        print("{}. {}".format(index+1,question))

    print('\n')

    print("ANSWERS")
    for index, answer in enumerate(answers):
        print("{}. {}".format(index+1,answer))

    print('\n')

    print("FEEDBACK")
    for index, text in enumerate(feedback):
        print("{}. {}".format(index+1,text))

    _exit = input("\nPRESS ENTER TO CLOSE")
    
if output_format == 'F':
    file = open(document_title+'.txt',"w+")
    file.write("Document: {}\n\n".format(document_title))

    file.write("QUESTIONS\n")
    for index, question in enumerate(questions):
        file.write("{}. {}".format(index+1,question))
        file.write("\n")
        
    file.write('\nANSWERS\n')
    file.write("If an answer does not 'appear', it is most likely too complex to be scarped\n")
    for index, answer in enumerate(answers):
        file.write("{}. {}".format(index+1,answer))
        file.write("\n")

    file.write('\nFEEDBACK\n')

    for index, text in enumerate(feedback):
        file.write("{}. {}".format(index+1,text))
        file.write("\n")
    file.close()
    print("File successfully closed")
