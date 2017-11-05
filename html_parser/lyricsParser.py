from bs4 import BeautifulSoup as bs
import requests
import re

class LyricsGroup():
        def __init__(self, addr):
                self.address = addr

        def setLyricsGroupLink(self, addr):
                self.address = addr

        def getLyricsGroupLink(self):
                return self.address

def buildLyrics(addr):
        s = LyricsGroup(addr)

        return s

def scrapeLyrics(sg, short_link):
        Lyrics_dict = {}
        container = {}

        artist_link = sg.getLyricsGroupLink()
        baseURL = sg.getLyricsGroupLink()
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

        page = requests.get(baseURL, headers=headers)
        
        text = r.text.encode('utf8')
        #soup = bs(text, 'html.parser')
        #source = soup.prettify()

        #source = source.encode('utf8').replace("<br>", "<br/>").replace("</br>", "")

        try:
                text2 = soup.getText()
                regex = r"\<\!\-\-\ Usage\ of\ azlyrics.com\ content\ by\ any\ third\-party\ lyrics\ provider\ is\ prohibited\ by\ our\ licensing\ agreement\.\ Sorry\ about\ that\.\ \-\-\>(.*)\<\!\-\-\ MxM\ banner\ \-\-\>"
                matches = re.finditer(regex, text, re.DOTALL)

                for matchNum, match in enumerate(matches):
                    Lyrics_dict[artist_link] = match.group(1)

        except:
                print('die')
                pass

        return Lyrics_dict
