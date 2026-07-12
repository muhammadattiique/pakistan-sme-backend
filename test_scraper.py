from scraper.downloader import Downloader
from scraper.parser import HTMLParser

url = "https://example.com"

downloader = Downloader()
html = downloader.download(url)

parser = HTMLParser()
soup = parser.parse(html)

print(soup.title.text)