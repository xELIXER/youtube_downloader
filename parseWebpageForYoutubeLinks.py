from bs4 import BeautifulSoup
import requests

def getYoutubeLinks(url, schemeForUrl):
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    file_obj = open("youtubeLinks.txt", "w")

    for a in soup.find_all('a', href=True):
        if a.text:
            href = a['href']
            if href.find(schemeForUrl) != -1:
                file_obj.write(a['href']+"\n")
    file_obj.close()
