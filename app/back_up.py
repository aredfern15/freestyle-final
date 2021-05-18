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

#team_id = [
#    {"teamID":20}
#]
#
#selected_id = input("Please input ID: ")
#matching_products = [p for p in team_id if str(p["teamID"]) == str(selected_id)]
#matching_product = matching_products[0]
#print("Selected team: " +"))
#
#quit()

team_name = input("Insert team name: ")

if team_name == "Twins":
    teamID = 0 

else:
    teamID = 1 

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



