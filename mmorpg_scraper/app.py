from typing import Optional
from mmorpg_scraper.scraper.scraper import Scraper
from mmorpg_scraper.scraper.game_list import game_list


def fetch_game_details(game_name: Optional[str] = None) -> dict:
    """
    Fetches game details from mmorpg.com 

    Usage:
        from mmorpg_scraper.app import fetch_game_details
        result = fetch_game_details("4story")
        print(result)

    Parameters:
        game_name: String game name e.g '4story'
        
    Return:    
        game_detail as dict.
    """
    scraper = Scraper(game_name)
    return scraper.fetch_game_details()

def fetch_game_list() -> dict:
    """
    Fetches game_list.

    Usage:
        from mmorpg_scraper.app import fetch_game_list
        result = fetch_game_list()
        print(result["games"][:50])

    Parameters:
        game_list as dict. game_list["games"] -> list
    """
    return game_list
