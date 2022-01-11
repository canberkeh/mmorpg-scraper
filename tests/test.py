import sys
sys.path.append('.')
from mmorpg_scraper.app import  fetch_game_list, fetch_game_details
from datetime import datetime
# TODO: Create more test. e2e tests needed.

ab = datetime.now()
"""
Return game_details

result = fetch_game_details('4story')
print(result)
"""


"""
Return game_list

result = fetch_game_list()
print(result)

"""



# with open("game_result2.txt", "r") as game_res:
#     lines = game_res.readlines()
#     lines = [line.rstrip() for line in lines]

# with open("test_json_result.txt", "w+") as json_result:
#     for i in lines:
#         i = i.strip("\'")
#         res = app(i)
#         json_result.write(res)
#         json_result.write("\n\n")
#         print(i + "done")
# a = app('elder-scrolls-online')
# print(a)  

ba = datetime.now()
print(ba-ab)


# 65 sayfayı gezip resultları tek tek aldırabiliriz.
# https://www.mmorpg.com/games-list/page/62