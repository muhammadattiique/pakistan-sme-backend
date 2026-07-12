import requests
from config import HEADERS, TIMEOUT


class Scraper:

    def download(self, url: str):

        try:

            response = requests.get(
                url,
                headers=HEADERS,
                timeout=TIMEOUT
            )

            response.raise_for_status()

            return response.text

        except Exception as e:

            print("Download Error:", e)

            return None