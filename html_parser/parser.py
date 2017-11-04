from lxml import html
import requests

baseURL = "https://www.azlyrics.com"
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

page = requests.get(baseURL, headers=headers)
tree = html.fromstring(page.content)

alphaLink = tree.xpath('//a[@class="btn btn-menu"]/text()')

print('Link: ', alphaLink)