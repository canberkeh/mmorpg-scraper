from typing import Dict, Optional
from mmorpg_scraper.scraper.scraper import Scraper
from mmorpg_scraper.scraper.game_list import game_list


def fetch_game_details(game_name: Optional[str] = None) -> str:
    """
    Fetches game details from mmorpg.com 

    :param game_name: String game name e.g '4story'
    :return: game_detail json object as string
    """
    scraper = Scraper(game_name)
    return scraper.fetch_game_details()

def fetch_game_list() -> dict:
    """
    Fetches game_list.

    :return: game_list as dict. game_list["games"] -> list
    """
    return game_list


# TODO: Create endpoint, create function for game_detail like game_detail('4story')