# from bs4 import BeautifulSoup as bs
# import requests as rq

# html_doc = rq.get("https://twitter.com/RAM_Maroc")
# #print(html_doc)
# soup = bs(html_doc.text, 'html.parser')
# #container = soup.find_all("article",class_="css-1dbjc4n r-1loqt21 r-18u37iz r-1ny4l3l r-1udh08x r-1yt7n81
#  #       r-ry3cjt r-o7ynqc r-6416eg")
# container = soup.find('a', {"class":"css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1ny4l3l"})
# print(container[0])

# import requests, bs4, webbrowser

url = 'https://twitter.com/RAM_Maroc'

# full_link = url 
# res = requests.get(full_link)
# soup = bs4.BeautifulSoup(res.text, "html.parser")
# # webbrowser.open(full_link)

# a = soup.findAll('main', {"class" : "})
# # {'class': 'css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1ny4l3l'})
# print(a)


from bs4 import BeautifulSoup
from urllib.request import urlopen

page = urlopen (url)
# print (page.read ())
soup = BeautifulSoup (page.read (), 'html5lib')

div = soup.find_all ('div', {'class' : 'css-1dbjc4n'})
# img = soup.find_all ('div', {'class' : 'css-1dbjc4n'})

print (div)