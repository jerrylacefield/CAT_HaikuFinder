from bs4 import BeautifulSoup as bs
import requests
import songsParser as songs

def getNextLink():
    print("Attempting to get the link...")
    resp = requests.get("http://172.25.21.208:8080/getLink", params={'type':'0'})
    print("Link has been gotten...")

    data = resp.json()
    return data['link']

def updateArtists(key, value):
	send = requests.post("http://172.25.21.208:8080/updateData", params={'link':key, 'data':value, 'type':'0'})

def finishArtists(link):
	send = requests.post("http://172.25.21.208:8080/finished", params={'link':link, 'type':'0'})

baseURL = "https://www.azlyrics.com"
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

mySongs = songs.buildSongs(baseURL + "/a/aaronlewis.html")
print(mySongs.getSongsGroupLink())

songs_dict = songs.scrapeSongs(mySongs)
print("songs group page scraped...")
