from doctest import OutputChecker
from email import header
from multiprocessing.sharedctypes import Value
import os
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url =  "https://practicalguidetoevil.wordpress.com/table-of-contents/"
title = "A Practical Guide to Evil"
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url)
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

# Create Directories for each Book and Generates Table of Contents .txt file
outPutFolder = "Output"
f = open('TOC.txt','w')
string = ''
for keys,values in linkDict.items():
    string+= keys+":"+values.text.replace(':','-')
    string+="---"
f.write(string)
f.close()
quit()
for keys in linkDict.keys():
    try:
        os.makedirs(outPutFolder+"/"+keys)
    except OSError as error:
        print(f'{keys} already exists!')
        continue

    for links in linkDict[keys].find_all('a'):
        stuff = links.get('href')
        print(f'Downloading: {links.text} from {stuff}')
        
        # Download the content here and filters
        chapter = requests.get(links.get('href'),headers=headers)
        chapterraw = BeautifulSoup(chapter.text,"html.parser")
        chaptertext = chapterraw.find(class_='entry-content')

        #Replaces illegal character
        chaptitle = links.text.replace(':','-')
        
        # Writes to .txt file
        f = open(outPutFolder+"/"+keys+"/"+chaptitle+".txt","w",encoding="utf-8")
        f.write(chaptitle + chaptertext.text)
        f.close
        time.sleep(2)
        print(f'Download of {links.text} successful!')

    

print("Folders created!")
# compile to epub
#I just realized that i have no TOC