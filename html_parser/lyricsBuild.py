from bs4 import BeautifulSoup as bs
import requests
import lyricsParser as Lyrics

def getNextLink():
	print("Attempting to get the link...")
	resp = requests.get("http://104.198.254.12:8080/getLink", params={'type':'2'})
	print("Link has been gotten...")

	data = resp.json()
	return data['link']


def updateLyricsByArtist(key, value1, value2):
	send = requests.post("http://104.198.254.12:8080/updateData", params={'link':key, 'data':value1, 'data':value2, 'type':'2'})

def finishLyrics(link):
	send = requests.post("http://104.198.254.12:8080/finished", params={'link':link, 'type':'2'})

baseURL = "https://www.azlyrics.com"
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }


link = " "
while link:
	link = getNextLink()
	# link = "/a/aaronlewis.html"
	
	myLyrics = Lyrics.buildLyrics(baseURL + link)
	print(myLyrics.getLyricsGroupLink())

	Lyrics_dict = Lyrics.scrapeLyrics(myLyrics, link)
	print("Lyrics page scraped for " + link)

	for key in Lyrics_dict:
		print(key, Lyrics_dict[key])
		# updateLyricsByArtist(Lyrics_dict[key][artist_link], key, Lyrics_dict[key][Lyric_title])

	print("Lyrics group page scraped for " + link + "...")
	link = ""
