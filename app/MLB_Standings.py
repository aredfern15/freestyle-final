import json
import os
from typing import KeysView
import requests
import time
from dotenv import load_dotenv 
#import pandas as pd    #most likely use 
import datetime  #most likely use 
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

list_of_team_names = []
for line in parsed_response: 
     list_of_team_names.append(line['Name'])
#print(list_of_team_names)

team = input("Please enter the team you would like to view: ")
capitalized_team = team.capitalize()
index = list_of_team_names.index(capitalized_team)
#print(index)

team_index = index 
city = parsed_response[team_index]["City"]
league = parsed_response[team_index]["League"]
name = parsed_response[team_index]["Name"]
division = parsed_response[team_index]["Division"]
wins = parsed_response[team_index]["Wins"]
losses = parsed_response[team_index]["Losses"]
division_rank = parsed_response[team_index]["DivisionRank"]
games_behind = parsed_response[team_index]["GamesBehind"]

named_tuple = time.localtime() 
time_string = time.strftime("%Y-%m-%d, %H:%M:%S", named_tuple)
run_time_date = datetime.datetime.now()
last_refreshed = ("RUN AT: " + run_time_date.strftime("%I:%M %p") + " on " + run_time_date.strftime("%B %d") + ", " + run_time_date.strftime("%Y"))


print("-------------------------")
print(f"Season: {season}")
print(f"SELECTED TEAM: {city} {name}")
print("-------------------------")
print("REQUESTING TEAM PERFORMANCE")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
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
