from bs4 import BeautifulSoup
import urllib.request

class url_html:
    def __init__(self,url) -> None:
        self.url = url 
    
    def crawl_html (url_html, element):
        url = url_html.url
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        return soup

    def crawl_by_tag(self, tag):
        url = self.url
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        elements = soup.find('section', class_='featured container clearfix').find_all(tag)
        return elements



