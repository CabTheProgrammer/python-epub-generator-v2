import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# TODO: Get contents of https://practicalguidetoevil.wordpress.com/table-of-contents/
url =  "https://practicalguidetoevil.wordpress.com/table-of-contents/"
response = requests.get(url)
# Parse to get links of each chapter per book, maybe use a dictionary or 2d array?
soup = BeautifulSoup(response.text,"html.parser")
linkslist=soup.find_all(class_='entry-content')

for link in linkslist:
    print(link.text)


# download each book and compile to epub