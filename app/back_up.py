import json
import os
from typing import KeysView
import requests
from dotenv import load_dotenv 
#import pandas as pd    #most likely use 
#from datetime import datetime  #most likely use 
load_dotenv()


season = input("Please enter the season you would like to view the MLB standings (2020 or 2021): ")

if season == "2020" or "2021": 
     pass
else: 
     print("Oops, you have entered an invalid season. Please try again with a symbol such as '2020' or '2021'.")
     exit()

#check if season has a season 
api_key = os.environ.get("api_key") 
request_url = f"https://fly.sportsdata.io/v3/mlb/scores/json/Standings/{season}?key={api_key}"
response = requests.get(request_url)
#print(type(response))
#print(response.status_code)
#print(response.text)
parsed_response = json.loads(response.text)
print(parsed_response)


print(parsed_response[0]["GamesBehind"])





#print("-------------------------")
#print(f"PRINT: {YEAR}")
#print(f"SELECTED TEAM: {CITY} {TEAM}")
#print("-------------------------")
#print("REQUESTING TEAM PERFORMANCE")
#print(f"REQUEST AT: {dt_string}")
#print("-------------------------")
#print(f"LATEST DAY: {LAST_REFRESHED}")
#print(f"LEAGUE: {LEAGUE}")
#print(f"DIVISION: {DIVISION}")
#print(f"WINS: {WINS}")
#print(f"LOSSES {LOSSES}")
#print(f"DIVISION RANK: {DIVISION_RANK}")
#print(f"GAMES BEHIND: {GAMES_BEHIND}")
#print(f"WRITING DATA TO CSV... {csv_file_path}")
#print("-------------------------")
#print("GO {TEAM}!") 
#print("-------------------------")
