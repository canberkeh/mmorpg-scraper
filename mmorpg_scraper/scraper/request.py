import requests
from mmorpg_scraper.scraper.headers_generator import headers
from mmorpg_scraper.scraper.constants import BASE_URL
from mmorpg_scraper.scraper.exceptions import ExtraHTTPError, NotFoundError


class SendRequest:
    def __init__(self, game_name: str):
        """ 
        Sends a get request with given game_name.
        Returns 404 or Status code if fails.
        Initializes response.
        
        :param game_name: game name to request.
        """
        try:
            self.response = requests.get(BASE_URL+game_name, headers=headers())
            if self.response.status_code == 404:
                raise NotFoundError("Url not found(404).")
        except:
            raise ExtraHTTPError(
                "Game not found. Status code {} returned.".format(self.response.status_code)
            )
