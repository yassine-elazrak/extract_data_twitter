from bs4 import BeautifulSoup as bs
import requests as rq

html_doc = rq.get("https://twitter.com/RAM_Maroc")
#print(html_doc)
soup = bs(html_doc.text, 'html.parser')
#container = soup.find_all("article",class_="css-1dbjc4n r-1loqt21 r-18u37iz r-1ny4l3l r-1udh08x r-1yt7n81
 #       r-ry3cjt r-o7ynqc r-6416eg")
container = soup.find('a', {"class":"css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1ny4l3l"})
print(container[0])
