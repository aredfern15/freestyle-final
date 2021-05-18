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
#print(parsed_response)

city = parsed_response[0]["City"]
league = parsed_response[0]["League"]
name = parsed_response[0]["Name"]
division = parsed_response[0]["Division"]
wins = parsed_response[0]["Wins"]
losses = parsed_response[0]["Losses"]
division_rank = parsed_response[0]["DivisionRank"]
games_behind = parsed_response[0]["GamesBehind"]


#key = parsed_response[0]["Key"]


#team = input("Please enter the team you would like to view: ")



#if team == "Twins":
#    TEAM = parsed_response[0]["Name"]
#else: print("nope, try again")





print("-------------------------")
print(f"Season: {season}")
print(f"SELECTED TEAM: {city} {name}")
print("-------------------------")
#print("REQUESTING TEAM PERFORMANCE")
#print(f"REQUEST AT: {dt_string}")
#print("-------------------------")
#print(f"LATEST DAY: {LAST_REFRESHED}")
print(f"LEAGUE: {league}")
print(f"DIVISION: {division}")
print(f"WINS: {wins}")
print(f"LOSSES {losses}")
print(f"DIVISION RANK: {division_rank}")
print(f"GAMES BEHIND: {games_behind}")
#print(f"WRITING DATA TO CSV... {csv_file_path}")
print("-------------------------")
print(f"GO {name}!") 
print("-------------------------")
