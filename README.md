# MMORPG-SCRAPER

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />

Mmorpg-Scraper scrapes and parses mmorpg game data from mmorpg.com with python.

## Installation
```
pip install mmorpg-scraper
```
## Usage
```python
from mmorpg_scraper import app
```

#### fetch_game_details

Fetch details of a mmorpg game.
fetch_game_details(game_name: string)
Options:
"game_name" is the game name on mmorpg.com to get details, e.g. "4story" for 4Story. fetch_game_details('4story')

```python
from mmorpg_scraper.app import fetch_game_details

result = fetch_game_details("4story")
print(result)
```

Result of print(result):

```
{
    "result": {
        "status": 200,
        "detail": "Success"
    },
    "name": "4Story",
    "publisher": "Gameforge GmbH ",
    "official_site": "http://en.4story.gameforge.com/",
    "genre": "MMORPG",
    "setting": "Fantasy",
    "pvp": "Yes",
    "classification": "Imported",
    "engine": "Custom",
    "style": "Unknown",
    "developer": "Zemi Interactive",
    "status": "Released",
    "release_date": "2007",
    "distribution": [
        "Download"
    ],
    "business_model": [
        "Free",
        "Item Mall"
    ],
    "platforms": [
        "Android",
        "PC",
        "iOS"
    ],
    "rating": {
        "rating": 7.2,
        "vote_count": 37
    },
    "overview": "\n4Story Overview\n  \n4Story puts players in the three kingdoms of Iveria: DeFugel, Craxion, and Broa. Blessed by Rea, the Goddess of creation, these kingdoms have yet managed to bring war upon each other, all in an effort to force their \u2018truths\u2019 upon one another. Into this turmoil you are born, a hero destined to seek and find the real truth buried in hundreds of thousands of years of chaos and war.\nFEATURES\n\nTerritory Wars - At certain times each and every day, a \u2018territory war\u2019 will break out between two rival kingdoms. Fight in these wars for your kingdom, and if you can control of the territory, your kingdom\u2019s players will have access to more adventure locations and more opportunities to find treasures.\nEnormous Quests - 4Story comes complete with a grand main quest line, along with myriad sub and hidden quests.\nHidden Secrets - Within each quest are clues to finding a hidden, secret quest, an adventure-within-an-adventure, waiting for heroes to take the challenge of finding them.\nLegendary Weapons - Many of the weapons in 4Story are graded \u2018F\u2019 to \u2018SSS\u2019. These weapons can level with your character, and be upgraded to a maximum level of 24. 
Not only that, but the legendary options for these weapons may be transferred to other like weapons.\nR.S.T.S (Real-time Strategic Command System) - 4Story allows players to command up to 48 others, and is made possible by the unique R.S.T.S. system. Simply by using the minimap, a commander can monitor a real-time battle and fluidly issue orders just with mouse clicks.\nMounts - Mounts are almost always a more viable means of travel, and 4Story has them in abundance, from slow, easy-going mounts, to those that are as fast 
as the winds.\n\n"
}

```

#### fetch_game_list
Fetch game list in a dict. {"games": ["game1", "game2"...]}
```
from mmorpg_scraper.app import fetch_game_list

result = fetch_game_list()
print(result["games"][:50])
```

Result of print(result["games"][:50]):

```
['4story', '8bitmmo', '9dragons', '9lives-arena', 'a-tale-in-the-desert', 'a3', 'a3-still-alive', 'aberoth', 'ace-online', 'achaea', 'ad2460', 'adventure-land', 'adventure-quest-3d', 'adventurequest-worlds', 'aetolia-the-midnight-age', 'age-of-conan-unchained', 'age-of-the-four-clans', 'age-of-wushu', 'age-of-wushu-dynasty', 'agents-of-aggro-city-online', 'aika', 'aion', 'aion-classic', 'airside-andy', 'akanbar', 'albion-online', 'allods-online', 'alphadia-genesis', 'anarchy-online', 'angels-online', 'angry-birds-epic', 'animal-crossing-new-horizons', 'anime-ninja', 'anime-pirates', 'anocris', 'anthem', 'antilia', 'apb-reloaded', 'apex-legends', 'aranock-online', 'arcane-legends', 
'arcane-waters', 'arcfall', 'archeage', 'archeage-begins', 'archeage-unchained', 'archeblade', 'ark-survival-evolved', 'armed-heroes-2', 'armored-warfare']
```

## Changes
Change logs are here : [CHANGELOG.md](CHANGELOG.md)