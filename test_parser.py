from scraper import Scraper
from parser import BusinessParser

scraper = Scraper()

html = scraper.download("https://example.com")

parser = BusinessParser()

business = parser.parse(html)

print(business)