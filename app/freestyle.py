import json
import os
from typing import KeysView
import requests
from dotenv import load_dotenv 
#import pandas as pd    #most likely use 
#from datetime import datetime  #most likely use 

load_dotenv()


season = input("Please enter the season you would like to view the MLB standings: ")

if len(season) == 4: 
    pass
else: 
    print("Oops, you have entered an invalid season. Please try again with a symbol such as '2019'.")
    exit()

#check if season has a season 

api_key = os.environ.get("api_key") 
#request_url = f"https://fly.sportsdata.io/v3/mlb/scores/json/Standings/2021?key=5df11bf8ab924b3f8daa67c66e4e617c"
request_url = f"https://fly.sportsdata.io/v3/mlb/scores/json/Standings/2021?key={api_key}"
response = requests.get(request_url)

#print(type(response))
#print(response.status_code)
#print(response.text)


parsed_response = json.loads(response.text)
print(parsed_response)


quit()


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


##set up API_KEY and possibly default settings
#
#league = os.getenv("league", default="AL")
#division = os.getenv("division", default="East")
#team = os.getenv("team", default="Baltimore Orioles")
#app_env = os.getenv("APP_ENV", default="development")
#



#season_digits = False 

#for seasons in season: 
#    if seasons.isdigit(): 
#        season_digits = True

#if season_digits == False: 
#    pass
#else:
#    print("Oops, you have entered an invalid season with a digit. Please try again with a symbol such as 'IBM'.")
#    exit()

season = season







#define the league


#define the division


#define the team


#retrieve standings
