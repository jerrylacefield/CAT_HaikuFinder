from bs4 import BeautifulSoup as bs
import requests
import artists

baseURL = "https://www.azlyrics.com/"
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

myArtists = artists.createArtists(baseURL + 'a.html')	# create artists object
artists.scrapeArtists()

def getNextLink():
    resp = requests.get("http://localhost:8080/getLink", params={'type':'1'})
    data = resp.json()
    return data['link']
