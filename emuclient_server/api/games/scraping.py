from bs4 import BeautifulSoup
import requests


class GameScraping:

    @staticmethod
    def retrieve_gameslist_from_page(url: str) -> list[dict]:
        page = requests.get(url)
        soup = BeautifulSoup(page.content)

        tags = soup.find_all(class_="index gamelist")

        gamelist = []

        for tag in tags:
            gamelist.append({
                "title": tag.text, 
                "id": tag.get('href').split('/')[3]
            })

        return gamelist