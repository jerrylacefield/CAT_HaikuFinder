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

	try:
		songs = soup.find('div', id="listAlbum")
		# songs = soup.find('div', class_="col-xs-12 col-md-6 text-center")
		for link in songs.find_all('a', id=""):
			song_link = ink.get('href').encode('UTF8').replace("..","")
			songs_dict[song_link] = {}
			songs_dict[song_link]['artist_link'] = short_link.encode('UTF8')
			songs_dict[song_link]['song_title'] = link.string.encode('UTF8')



	except:
		pass

	return songs_dict