from enum import Enum


class StatusCode(Enum):
    Success = 200
    PartialContent = 206
    NotFound = 404


# BASE URL of mmorpg.com
BASE_URL = "https://www.mmorpg.com/"

# Distribution results from site.
distributions = ["Download", "Browser", "Retail"]

# Business model results from site.
business_models = ["Buy to Play", "Free", "Hybrid", "Item Mall", "Subscription"]

# Platform results from site.
platforms = ["3DS", "Android", "DreamCast", "Google Stadia", "iOS", "Linux", 
                "Mac", "Mobile Devices", "PC", "Playstation 2", "Playstation 4",
                "Playstation 5", "PS3", "Switch", "Vita", "Wii", "Wii U", "XBox",
                "XBox 360", "Xbox One", "Xbox Series X/S"]
