from bs4 import BeautifulSoup


class BusinessParser:

    def parse(self, html):

        soup = BeautifulSoup(html, "html.parser")

        title = soup.title.text if soup.title else ""

        return {
            "title": title
        }