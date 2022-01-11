from bs4 import BeautifulSoup
from mmorpg_scraper.scraper.game_detail import GameDetail
from mmorpg_scraper.scraper.request import SendRequest
from mmorpg_scraper.scraper.exceptions import ParsingError
from mmorpg_scraper.scraper.constants import (
    StatusCode,
    distributions,
    business_models,
    platforms
)


class Scraper:
    def __init__(self, game_name: str):
        """
        Initializes GameDetail object.
        Sends request with given game_name.
        Parses response.content with bs4.
           
        :param game_name: String game_name to 
        execute process.
        """
        self.game_detail = GameDetail()
        self.request = SendRequest(game_name)
        self.soup = BeautifulSoup(self.request.response.content, 'html.parser')


    def fetch_game_details(self) -> str: # TODO: Improvements needed. Exceptions should handled.
        """
        Executes parsing to mmorpg.com.
        :return: game detail object as JSON.
        """
        try:
            self.parse_name()
            self.parse_publisher_and_official_site()
            self.parse_genre()
            self.parse_distribution_and_business_model()
            self.parse_platform()
            self.parse_rating()
            self.parse_vote_count()
            self.parse_overview()
        except:
            raise ParsingError("Can not parse publisher.")
        finally:
            self.set_status_code()
            return self.game_detail.to_json()


    def parse_name(self) -> None:
        """
        Parse name for game_detail.name
        """
        try:
            self.game_detail.name  = self.soup.find("div", {"class": "game-info__top-title-wrap"}).h1.text
        except:
            pass


    def parse_publisher_and_official_site(self) -> None:
        """
        Parse publisher and official site for
        game_detail.publisher and game_detail.official_site
        """
        try:
            self.game_detail.publisher = self.soup.find("p", {"title": "Publisher"}).text.partition("|")[0]
            self.game_detail.official_site = self.soup.find("p", {"title": "Publisher"}).a['href']
        except:
            pass     


    def parse_genre(self) -> None:  # TODO: IMPROVEMENTS NEEDED.
        """
        Parse genre, setting, pvp, classification, engine, style,
        developer, status and release date for game_detail object.
        """
        try:
            strongs = [strong.text for strong in self.soup.find(class_='game-info__middle').find_all('strong')]
            self.game_detail.genre = strongs[0]
            self.game_detail.setting = strongs[1]
            self.game_detail.pvp = strongs[2]
            self.game_detail.classification = strongs[3]
            self.game_detail.engine = strongs[4]
            self.game_detail.style = strongs[5]
            self.game_detail.developer = strongs[6]
            self.game_detail.status = strongs[7]
            self.game_detail.release_date = strongs[8]
        except:
            pass

    def parse_distribution_and_business_model(self) -> None:
        """
        Parse distribution and business model for game_detail object.
        """
        try:
            for element in self.soup.find(class_='game-info__middle').find_all('i'):
                if element.get('title') in distributions and element.get('title') not in self.game_detail.distribution:
                    self.game_detail.distribution.append(element.get('title'))
                elif element.get('title') in business_models and element.get('title') not in self.game_detail.business_model:
                    self.game_detail.business_model.append(element.get('title'))
        except:
            pass

    def parse_platform(self) -> None:
        """
        Parse platform for game_detail.platform
        """
        try:
            for element in self.soup.find(class_='game-info__button').find_all('i'):   
                if element.get('title') in platforms and element.get('title') not in self.game_detail.platforms:
                    self.game_detail.platforms.append(element.get('title'))
        except:
            pass
        

    def parse_rating(self) -> None:
        """
        Parse rating for game_detail.rating["rating"]
        """
        try:
            self.game_detail.rating["rating"] = float(self.soup.find(class_='game-info__button').find('strong').text)
        except:
            pass


    def parse_vote_count(self) -> None:
        """
        Parse vote_count for game_detail.rating["vote_count"]
        """
        try:
            self.game_detail.rating["vote_count"] = int(self.soup.find(class_='user-rating__head-title').find('span').text)
        except:
            pass


    def parse_overview(self) -> None:
        """
        Parse overview for game_detail.overview
        """
        try:
            for element in self.soup.find('article'):
                self.game_detail.overview += element.text
        except:
            pass

    def set_status_code(self) -> None: # TODO: When expection raises, add can not parsed category to detail.
        """
        Parse status code and details for game_detail.result.
        """
        if self.game_detail.result["detail"]:
            self.game_detail.result["status"] = StatusCode.PartialContent.value
        else:
            self.game_detail.result["status"], self.game_detail.result["detail"] = StatusCode.Success.value, "Success"
