from bs4 import BeautifulSoup as bs
import requests

baseURL = "https://www.azlyrics.com/a.html"
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

page = requests.get(baseURL, headers=headers)

soup = bs(page.text, 'html.parser')
#soup = soup.encode('utf8').replace("<br>", "<br/>")
source = soup.prettify()

source = source.encode('utf8').replace("<br>", "<br/>").replace("</br>", "").replace("\t","")




#print('Link: ', alphaLink)
