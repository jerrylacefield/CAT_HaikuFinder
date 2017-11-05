from bs4 import BeautifulSoup as bs
import requests

class ArtistsGroup():
	artists = {}

	def __init__(self, addr):
		self.address = addr

	def setArtistsGroupLink(self, addr):
		self.address = addr

	def getArtistsGroupLink(self):
		return self.address

def createArtists(addr):
	a = ArtistsGroup(addr)

	return a

def scrapeArtists():
	artists_dict = {}

	baseURL = "https://www.azlyrics.com/a.html"
	headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

	page = requests.get(baseURL, headers=headers)
	soup = bs(page.text, 'html.parser')
	source = soup.prettify()

	source = source.encode('utf8').replace("<br>", "<br/>").replace("</br>", "")

	arts = soup.find('div', class_="col-sm-6 text-center artist-col")
	for link in arts.find_all('a'):
		# artist_name = 
		# print(link.get('href').encode('UTF8'), link.string.encode('UTF8'))
		artists_dict[link.get('href').encode('UTF8')] = link.string.encode('UTF8')

	for key in artists_dict:
		print(key + " --> " + artists_dict[key])