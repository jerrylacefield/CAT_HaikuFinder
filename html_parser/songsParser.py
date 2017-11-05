from bs4 import BeautifulSoup as bs
import requests

class SongsGroup():
	def __init__(self, addr):
		self.address = addr

	def setSongsGroupLink(self, addr):
		self.address = addr

	def getSongsGroupLink(self):
		return self.address

def buildSongs(addr):
	s = SongsGroup(addr)

	return s

def scrapeSongs(sg, short_link):
	songs_dict = {}
	container = {}

	artist_link = sg.getSongsGroupLink()
	# baseURL = sg.getSongsGroupLink()
	headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

	page = requests.get(artist_link, headers=headers)
	soup = bs(page.text, 'html.parser')
	source = soup.prettify()

	source = source.encode('utf8').replace("<br>", "<br/>").replace("</br>", "")
	songs = soup.find('div', id="listAlbum")
	for link in songs.find_all('a', id=""):
		# print(link.get('href').encode('UTF8'), link.string.encode('UTF8'))
		container["artist_link"] = short_link
		container["song_title"] = link.string.encode('UTF8')

		songs_dict[link.get('href').encode('UTF8').replace("..","")] = container

	return songs_dict