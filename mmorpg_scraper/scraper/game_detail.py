import json
from typing import Optional


class GameDetail:
    """ Creates game_detail object. """
    def __init__(self,
                 response: Optional[int] = None,
                 response_detail: Optional[str] = None,
                 name: Optional[str] = None,
                 publisher: Optional[str] = None,
                 official_site: Optional[str] = None,
                 genre: Optional[str] = None,
                 setting: Optional[str] = None,
                 pvp: Optional[str] = None,
                 classification: Optional[str] = None,
                 engine: Optional[str] = None,
                 style: Optional[str] = None,
                 developer: Optional[str] = None,
                 status: Optional[str] = None,
                 release_date: Optional[str] = None,
                 distribution: Optional[list] = [],
                 business_model: Optional[list] = [],
                 platforms: Optional[list] = [],
                 rating: Optional[float] = None,
                 vote_count: Optional[int] = None,
                 overview: Optional[str] = ""):
        self.result = {"status" : response, "detail" : response_detail}
        self.name = name
        self.publisher = publisher
        self.official_site = official_site
        self.genre = genre
        self.setting = setting
        self.pvp = pvp
        self.classification = classification
        self.engine = engine
        self.style = style
        self.developer = developer
        self.status = status
        self.release_date = release_date
        self.distribution = distribution
        self.business_model = business_model
        self.platforms = platforms
        self.rating = {"rating": rating, "vote_count": vote_count}
        self.overview = overview

    def to_json(self) -> str:
        """Returns game_detail object as Json object.

        :return: a dictionary of game_details
        """
        return json.dumps(self, default=lambda o: o.__dict__,
                          indent=4)
