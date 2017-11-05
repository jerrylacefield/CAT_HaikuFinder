from bs4 import BeautifulSoup as bs
import requests
import songsParser as songs

def getNextLink():
    print("Attempting to get the link...")
    resp = requests.get("http://104.198.254.12:8080/getLink", params={'type':'1'})
    print("Link has been gotten...")

    data = resp.json()
    return data['link']


def updateSongsByArtist(key, value1, value2):
	send = requests.post("http://104.198.254.12:8080/updateData", params={'link':key, 'data':value1, 'data':value2, 'type':'1'})

def finishSongs(link):
	send = requests.post("http://104.198.254.12:8080/finished", params={'link':link, 'type':'1'})

baseURL = "https://www.azlyrics.com"
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }


link = " "
while link:
	link = getNextLink()
	# link = "/a/aaronlewis.html"
	
	mySongs = songs.buildSongs(baseURL + link)
	print(mySongs.getSongsGroupLink())

	songs_dict = songs.scrapeSongs(mySongs, link)
	print("songs page scraped for " + link)

	for key in songs_dict:
		updateSongsByArtist(songs_dict[key][artist_link], key, songs_dict[key][song_title])

	print("songs group page scraped for " + link + "...")
	link =""
