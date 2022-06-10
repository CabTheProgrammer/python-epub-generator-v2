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

linkarray = []
titlearray = []
for books in linkslist.find_all('h2'):
    print(books.text)
    titlearray.append(books.text)

print(titlearray)
    



# download each book and compile to epub