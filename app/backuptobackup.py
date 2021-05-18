import json
import os
from typing import KeysView
import requests
from dotenv import load_dotenv 
#import pandas as pd    #most likely use 
import datetime 
load_dotenv()
api_key = os.environ.get("api_key") 

season = input("Please enter the season you would like to view the MLB standings (2020 or 2021): ")
if season == "2020" or "2021": 
     pass
else: 
     print("Oops, you have entered an invalid season. Please try again with a year such as '2020' or '2021'.")
     exit()

team = input("Please enter the team you would like to view: ")
capitalized_team = team.title()
list_of_team_names = []

if season == '2020': 
     request_url = f"https://fly.sportsdata.io/v3/mlb/scores/json/Standings/{season}?key={api_key}"
     response = requests.get(request_url)
     parsed_response = json.loads(response.text)
     for line in parsed_response: 
          list_of_team_names.append(line['Name'])
     team_index = list_of_team_names.index(capitalized_team)
     print(list_of_team_names)
else:
     request_url = f"https://fly.sportsdata.io/v3/mlb/scores/json/Standings/{season}?key={api_key}"
     response = requests.get(request_url)
     parsed_response = json.loads(response.text)
     for line in parsed_response: 
          list_of_team_names.append(line['Name'])
     team_index = list_of_team_names.index(capitalized_team)

city = parsed_response[team_index]["City"]
league = parsed_response[team_index]["League"]
name = parsed_response[team_index]["Name"]
division = parsed_response[team_index]["Division"]
wins = parsed_response[team_index]["Wins"]
losses = parsed_response[team_index]["Losses"]
division_rank = parsed_response[team_index]["DivisionRank"]
games_behind = parsed_response[team_index]["GamesBehind"]


print("-------------------------")
print(f"SEASON: {season}")
print(f"SELECTED TEAM: {city} {name}")
print("-------------------------")
import time
named_tuple = time.localtime() 
time_string = time.strftime("%Y-%m-%d, %H:%M:%S", named_tuple)
run_time_date = datetime.datetime.now()
print("RUN AT: " + run_time_date.strftime("%I:%M %p") + " on " + run_time_date.strftime("%B %d") + ", " + run_time_date.strftime("%Y"))
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

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "standings.csv")

csv_headers = ["City", "League", "Name", "Division", "Wins", "Losses", "DivisionRank", "GamesBehind"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "City": date,
            "League": daily_prices["1. open"],
            "Name": daily_prices["2. high"], 
            "Division": daily_prices["3. low"],
            "Wins": daily_prices["4. close"],
            "Losses": daily_prices["5. volume"], 
            "DivisionRank": daily_prices[], 
            "GamesBehind": daily_prices[],     
        })

