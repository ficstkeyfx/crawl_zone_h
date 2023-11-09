from bs4 import BeautifulSoup
import urllib.request

url =  'https://zone-h.org/mirror/id/40325449'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
print(soup)