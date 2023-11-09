# import urllib
# import urllib3
# import string
# import sys
# from bs4 import BeautifulSoup

# hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
# values = {'query' : '5ed10c844ed4266a18d34e2ba06b381a' }
# # data = urllib.urlencode(values)
# request = urllib3.request("https://defacer.id", headers=hdr)
# response = urllib3.urlopen(request)
# the_page = response.read()
# pool = BeautifulSoup(the_page)
import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'https://defacer.id')
print(r.status)
print( r.headers)
print(r.data)
# print (pool)