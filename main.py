from os import link
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
    print(books.text)
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
    print(f'I is {i}')
    # print(f'{titlearray[x]}')
    # print(i)
    # print(children[i])
    print('---------')
    
    # if(i==6):
    #      break
    linkDict[titlearray[x]]=children[i]
    x+=1
    
print(linkDict) 



# Create Directories for each Book
# download each book and compile to epub