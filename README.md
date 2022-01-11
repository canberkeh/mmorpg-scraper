# MMORPG-SCRAPER

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

Mmorpg-Scraper scrapes and parses Mmorpg game data from mmorpg.com with python.

## Installation
```
pip install mmorpg-scraper
```
## Usage
Game list can be found in json file.  
* fetch_game_details: Fetch a games details. 


#### fetch_game_details

Fetch a games details.
fetch_game_details(game_name: string)
Options:

"game_name" is the game name on mmorpg.com to get details, e.g. "4story" for 4Story. get_game_detail('4story')
