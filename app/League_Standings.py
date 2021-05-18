import json
import os
from typing import KeysView
import requests
import time
from dotenv import load_dotenv 
#import pandas as pd    #most likely use 
import datetime  #most likely use 
load_dotenv()

sport = input("Please enter the league (MLB, NBA, NFL, NHL) you would like to view the 2020/2021 standings of: ")


valid_sports = ['MLB', 'NBA', 'NFL', 'NHL']
is_valid = sport not in valid_sports
try:
  if is_valid == True: 
    raise ValueError()
except ValueError:
    print("Please enter a valid league: ")
    exit()

#if sport == "MLB" or "NBA" or "NHL":
#     pass
#else:
#     print("The 2021 NFL season has not occured yet. Please select another league or year. Thank you.")


#
#season = input("Please enter the season you would like to view the MLB standings (2020 or 2021): ")
#if season == "2020" or "2021": 
#     pass
#else: 
#     print("Oops, you have entered an invalid season. Please try again with a symbol such as '2020' or '2021'.")
#     exit()
#
##check if season has a season 

if sport == 'MLB':
     api_key = os.environ.get("api_key")
elif sport == 'NBA':
     api_key = os.environ.get("api_key_nba")
elif sport == 'NHL': 
     api_key = os.environ.get("api_key_nhl")
elif sport == 'NFL':
     api_key = os.environ.get("api_key_nfl")

#api_key = os.environ.get("api_key") 
request_url = f"https://fly.sportsdata.io/v3/{sport}/scores/json/Standings/2020?key={api_key}"
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
if sport == 'MLB': 
     league = parsed_response[team_index]["League"]
else:
     league = parsed_response[team_index]["Conference"]
name = parsed_response[team_index]["Name"]
division = parsed_response[team_index]["Division"]
wins = parsed_response[team_index]["Wins"]
losses = parsed_response[team_index]["Losses"]
division_rank = parsed_response[team_index]["DivisionRank"]

if sport == 'MLB':
     games_behind = parsed_response[team_index]["GamesBehind"]
elif sport == 'NBA': 
     games_behind = parsed_response[team_index]["GamesBack"]
elif sport == 'NHL':
     games_behind = print("N/A")

named_tuple = time.localtime() 
time_string = time.strftime("%Y-%m-%d, %H:%M:%S", named_tuple)
run_time_date = datetime.datetime.now()
last_refreshed = ("RUN AT: " + run_time_date.strftime("%I:%M %p") + " on " + run_time_date.strftime("%B %d") + ", " + run_time_date.strftime("%Y"))


print("-------------------------")
#print(f"Season: {season}")
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

