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

def scrapeSongs(sg):
	songs_dict = {}

	artist_link = "https://www.azlyrics.com/a/aaronlewis.html"
	# baseURL = sg.getSongsGroupLink()
	headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

	page = requests.get(artist_link, headers=headers)
	soup = bs(page.text, 'html.parser')
	source = soup.prettify()

	source = source.encode('utf8').replace("<br>", "<br/>").replace("</br>", "")

	songs = soup.find('div', id="listAlbum")
	for child in songs.children:
		songs2 = songs.find_all('a')
		# for link in songs2.content:
		# 	print(link.get('href').encode('UTF8'))


	# for link in songs.find_all('a'):
	# 	print(link.get('href').encode('UTF8'), link.string.encode('UTF8'))
	# 	# songs_dict[link.get('href').encode('UTF8')] = link.string.encode('UTF8')

	# return songs_dict