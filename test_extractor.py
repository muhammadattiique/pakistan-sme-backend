from scraper.downloader import Downloader
from scraper.parser import HTMLParser
from scraper.extractor import BusinessExtractor

url = "https://www.businesslist.pk/companies/business-directory"

downloader = Downloader()

html = downloader.download(url)

parser = HTMLParser()

soup = parser.parse(html)

extractor = BusinessExtractor()

businesses = extractor.extract(soup)

print(businesses)