import unittest
import requests
import sys
from bs4 import BeautifulSoup
sys.path.append('.')
from mmorpg_scraper.scraper.headers_generator import headers
from mmorpg_scraper.scraper.constants import BASE_URL

skip_list  = ["/final-fantasy-xiv", "/guild-wars-2", "/elder-scrolls-online", "/secret-world-legends",
"/darkfall-rise-of-agon", "/warframe", "/final-fantasy-xiv",
"/guild-wars-2",
"/elder-scrolls-online",
"/secret-world-legends",
"/darkfall-rise-of-agon",
"/warframe",
"/blue-protocol",
"/lost-ark",
"/ashes-of-creation",
"/pantheon-rise-of-the-fallen",
"/fractured",
"/dual-universe",
"/lineage2m",
"/final-stand-ragnarok",
"/mechwarrior-5-mercenaries",
"/star-wars-kotor-remake",
"/iron-conflict",
"/cinderstone-online",
"/fractured",
"/broken-ranks",
"/chronicles-of-elyria",
"/embers-adrift",
"/lost-ark",
"/zy-universe",
"/broken-ranks",
"/mortal-online-2",
"/broken-ranks",
"/pokemon-legends-arceus",
"/elteria-adventures",
"/lost-ark"]
with open("game_result2.txt", "w+") as game_result:

    for i in range(1,64):
        response = requests.get(BASE_URL+ "games-list/page/"+str(i), headers=headers())  # indent
        soup = BeautifulSoup(response.content, 'html.parser')  #indent
        divs = soup.find_all("div", {"class": "card-i__title"})
        for i in divs:  
            if i.h3.a["href"] in skip_list:
                pass
            else:
                skip_list.append(i.h3.a["href"])
                res ="'" + i.h3.a["href"][1::] + "'" 
                game_result.write(res)
                game_result.write("\n")
            
# card-i__title
# with open("html_reader.txt", "w+") as txt:
#     txt.write(str(soup))
    
