import json
import os
from typing import KeysView
import requests
from dotenv import load_dotenv 
import csv
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

team_name = [
    {"Name": "Twins", "TeamID": 0},
    {"Name": "Indians", "TeamID": 1},
    {"Name": "White Sox", "TeamID": 2},
    {"Name": "Royals", "TeamID": 3},
    {"Name": "Tigers", "TeamID": 4},
    {"Name": "Rays", "TeamID": 5},
    {"Name": "Yankees", "TeamID": 6},
    {"Name": "Blue Jays", "TeamID": 7},
    {"Name": "Orioles", "TeamID": 8},
    {"Name": "Red Sox", "TeamID": 9},
    {"Name": "Athletics", "TeamID": 10},
    {"Name": "Astros", "TeamID": 11},
    {"Name": "Mariners", "TeamID": 12},
    {"Name": "Angels", "TeamID": 13},
    {"Name": "Rangers", "TeamID": 14},
    {"Name": "Cubs", "TeamID": 15},
    {"Name": "Cardinals", "TeamID": 16},
    {"Name": "Reds", "TeamID": 17},
    {"Name": "Brewers", "TeamID": 18},
    {"Name": "Pirates", "TeamID": 19},
    {"Name": "Braves", "TeamID": 20},
    {"Name": "Marlins", "TeamID": 21},
    {"Name": "Phillies", "TeamID": 22},
    {"Name": "Mets", "TeamID": 23},
    {"Name": "Nationals", "TeamID": 24},
    {"Name": "Dodgers", "TeamID": 25},
    {"Name": "Padres", "TeamID": 26},
    {"Name": "Giants", "TeamID": 27},
    {"Name": "Rockies", "TeamID": 28},
    {"Name": "Diamondbacks", "TeamID": 29},
]

selected_name = input("Please input a MLB team name (i.e. 'Red Sox' or 'Nationals): ")
matching_products = [p for p in team_name if str(p["Name"]) == str(selected_name)]
matching_product = matching_products[0]
teamID = matching_product["TeamID"]

#print(teamID)



city = parsed_response[teamID]["City"]
league = parsed_response[teamID]["League"]
name = parsed_response[teamID]["Name"]
division = parsed_response[teamID]["Division"]
wins = parsed_response[teamID]["Wins"]
losses = parsed_response[teamID]["Losses"]
division_rank = parsed_response[teamID]["DivisionRank"]
games_behind = parsed_response[teamID]["GamesBehind"]


##csv_file_path = "data/teams.csv" # a relative filepath
#csv_file_path=os.path.join(os.path.dirname(__file__), "..", "data", "monthly_sales.csv")
#
#with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
#    writer = csv.DictWriter(csv_file, fieldnames=["city", "name"])
#    writer.writeheader() # uses fieldnames set above
#
#
#    writer.writerow({
#        "timestamp": "",
#        "open": "",
#        "high": "",
#        "low": "",
#
#    })
#
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



