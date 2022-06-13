from doctest import OutputChecker
from email import header
import os
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# TODO: Get contents of https://practicalguidetoevil.wordpress.com/table-of-contents/
url =  "https://practicalguidetoevil.wordpress.com/table-of-contents/"
title = "A Practical Guide to Evil"

response = requests.get(url)
# Parse to get links of each chapter per book, maybe use a dictionary or 2d array?
soup = BeautifulSoup(response.text,"html.parser")
linkslist=soup.find(class_='entry-content')

linkDict = {}  #Dictionary to hold books and links to each chapter
titlearray = []
for books in linkslist.find_all('h2'):
    titlearray.append(books.text)


# title array holds all the book titles

# for i in range(len(linkslist.find_all('li'))):
#     #adding to book 1
#     barray.append(linkslist.find_all('li')[i])
#     linkarray[titlearray[x]]=barray
#     if linkslist.find_all('li')[i].text == "Epilogue":
#         x+=1 
#         barray=[]

children = linkslist.findChildren('ul')
x=0
for i in range(len(children)-1):
# for child in children:
    if(i==1):
        continue
    # print(f'I is {i}')
    # print(f'{titlearray[x]}')
    # print(i)
    # print(children[i])
    # print('---------')
    
    # if(i==6):
    #      break
    linkDict[titlearray[x]]=children[i]
    x+=1
    
# print(len(linkDict[titlearray[0]].values)) 

# Create Directories for each Book
outPutFolder = "Output"
for keys in linkDict.keys():
    # TODO: Create directories for books [x]
    # try:
    #     os.makedirs(outPutFolder+"/"+keys)
    # except OSError as error:
    #     print(f'{keys} already exists!')
    #     continue

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/39.0.2171.95 Safari/537.36'}


    for links in linkDict[keys].find_all('a'):
        #TODO: downloadcontent
        stuff = links.get('href')
        print(f'Downloading: {links.text} from {stuff}')
        
        # Download the content here and filters
        chapter = requests.get(links.get('href'),headers=headers)
        chapterraw = BeautifulSoup(chapter.text,"html.parser")
        chaptertext = chapterraw.find(class_='entry-content')
        print(chaptertext.text)

        #Replaces illegal character
        chaptitle = links.text.replace(':','-')
        
        # Writes to .txt file
        f = open(chaptitle+".txt","w",encoding="utf-8")
        f.write(chaptitle + chaptertext.text)
        f.close
        break

    break

print("Folders created!")
# compile to epub