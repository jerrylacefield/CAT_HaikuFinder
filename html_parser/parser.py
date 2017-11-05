from bs4 import BeautifulSoup as bs
import requests
import artists

def getNextLink():
    resp = requests.get("http://localhost:8080/getLink", params={'type':'0'})
    data = resp.json()
    return data['link']

def updateArtists(k, v):
	send = requests.post("http://localhost:8080/updateData", params={'link':k, 'data':v, 'type':'0'})

baseURL = "https://www.azlyrics.com"
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

while True:
		myArtists = artists.createArtists(baseURL + "/a.html")	# create artists object
		artists_dict = artists.scrapeArtists(myArtists)

		for key in artists_dict:
			updateArtists(key, artists_dicts[key])

		break

