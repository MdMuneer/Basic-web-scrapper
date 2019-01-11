import requests
from bs4 import BeautifulSoup
import csv

f= csv.writer(open('names.csv' ,'w'))
f.writerow(['NAME','LINK'])


url="http://www.espncricinfo.com/india/content/player/country.html?country=6;alpha=A"
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')

artist_name_list = soup.find(class_='ciPlayerbycapstable')
artist_name_list_items = artist_name_list.find_all('a')

for artist_name in artist_name_list_items:
    names = artist_name.contents
    links = 'http://www.espncricinfo.com/india/content/player' + artist_name.get('href')

    f.writerow([names,links])
