import json
import os
from typing import KeysView
import requests
from dotenv import load_dotenv 
#import pandas as pd    #most likely use 
#from datetime import datetime  #most likely use 

load_dotenv()

TEAM_NAME = os.getenv("TEAM_NAME", default="Orioles")
APP_ENV = os.getenv("APP_ENV", default="development")

def set_team_name():
    if APP_ENV == "development":
        user_team_name = input("PLEASE INPUT THE TEAM YOU WOULD LIKE TO SEE: ")
    else:
        user_team_name = TEAM_NAME
    return user_team_name

# wanted to include previous seasons, but had to pay for premium package 
def get_Standings():
    request_url = f"https://fly.sportsdata.io/v3/mlb/scores/json/Standings/2021?key={api_key}"
    response = requests.get(request_url)
    if response.status_code != 200:
        return None
    parsed_response = json.loads(response.text)



if __name__ == "__main__":

    print(f"RUNNING THE STATS RETREIVER IN {APP_ENV.upper()} MODE...")

    # CAPTURE INPUTS

    user_team_name = set_team_name()
    print("TEAM NAME:", user_team_name)

    # FETCH DATA

    result = get_Standings(user_team_name=TEAM_NAME)
    if not result:
        print("INVALID TEAM NAME. PLEASE CHECK YOUR INPUTS AND TRY AGAIN!")
        exit()

    # DISPLAY OUTPUTS

    print("-----------------")
    print(f"THIS YEAR'S STATS FOR {result['user_team_name'].upper()}...")
    print("-----------------")

    for team_standing in result["get_Standings"]:
        print(team_standing)







#season = input("Please enter the season you would like to view the MLB standings: ")

# if len(season) == 4: 
#     pass
# else: 
#     print("Oops, you have entered an invalid season. Please try again with a symbol such as '2019'.")
#     exit()

#check if season has a season 

#api_key = os.environ.get("api_key") 
#request_url = f"https://fly.sportsdata.io/v3/mlb/scores/json/Standings/2021?key={api_key}"
#response = requests.get(request_url)

#print(type(response))
#print(response.status_code)
#print(response.text)


# parsed_response = json.loads(response.text)
# print(parsed_response)


# quit()


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

#season = season




#define the league


#define the division


#define the team


#retrieve standings
