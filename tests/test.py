import unittest
import sys
sys.path.append('.')
from mmorpg_scraper import app


class TestScraper(unittest.TestCase):

    def testing_game_list(self):
        result = app.fetch_game_list()
        self.assertGreaterEqual(len(result["games"]), 900)
    
    
    def testing_game_detail(self):
        # Testing for game name --> 9dragons
        result = app.fetch_game_details("9dragons")
        self.assertIs(dict, type(result))
        self.assertEqual(result["result"]["status"], 200)
        self.assertEqual(result["result"]["detail"], "Success")
        self.assertEqual(result["name"], "9Dragons")
        self.assertGreaterEqual(len(result["publisher"]), 2)
        self.assertGreaterEqual(len(result["official_site"]), 2)
        self.assertGreaterEqual(len(result["genre"]), 2)
        self.assertGreaterEqual(len(result["setting"]), 2)
        self.assertGreaterEqual(len(result["pvp"]), 1)
        self.assertGreaterEqual(len(result["setting"]), 2)
        self.assertGreaterEqual(len(result["classification"]), 2)
        self.assertGreaterEqual(len(result["engine"]), 2)
        self.assertGreaterEqual(len(result["style"]), 2)
        self.assertGreaterEqual(len(result["developer"]), 2)
        self.assertGreaterEqual(len(result["status"]), 2)
        self.assertGreaterEqual(len(result["release_date"]), 2)
        self.assertGreaterEqual(len(result["distribution"]), 1)
        self.assertGreaterEqual(len(result["business_model"]), 1)
        self.assertGreaterEqual(len(result["platforms"]), 1)
        self.assertGreaterEqual(result["rating"]["rating"], 0.1)
        self.assertGreaterEqual(result["rating"]["vote_count"], 1)
        self.assertGreaterEqual(len(result["overview"]), 10)

if __name__=="__main__":
    unittest.main()
