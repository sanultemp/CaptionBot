import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "2005175873:AAFFL37QqTP0cat_PsEhU5zqVRWeJIgp574")
      API_ID = int(os.environ.get("APP_ID", 7469109))
      API_HASH = os.environ.get("API_HASH", "4d4023337b8cc46c306af69adb5fc21a")
      CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "@Mo_Tech_YT @Mo_Tech_Group")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "MrTonyStarKing")
