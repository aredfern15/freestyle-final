import json
import csv
import os
from typing import KeysView
import requests
import time
from dotenv import load_dotenv 
import datetime  
load_dotenv()


sport_league = input("Please enter the league (MLB, NBA, NFL, NHL) you would like to view the 2020/2021 standings of: ")
sport_league = sport_league.upper()

valid_leagues = ['MLB', 'NBA', 'NFL', 'NHL']

"""
This is the first major step of the model--selecting a professional sports league to research. If the user inputs a correct 
league, it will move to the next step. If it is an invalid team, the system will quit gracefully and you can start over.
"""

is_valid = sport_league not in valid_leagues
try:
     if is_valid == True: 
          raise ValueError()
except ValueError:
     print("Please enter a valid league. ")
     exit()
season = input("Please enter the season you would like to view the standings for (i.e., 2020 or 2021): ")

"""
This is the second major step of the model--selecting a year. While it would be nice to research any sports year, the
free API services only provides years 2020 and 2021. The user will need to select a year they're interested in. If they
select an invalid year, then the system will quit gracefully.
"""

if sport_league == "NFL":
     if season == "2021":
          print("Oops, the 2021 season for NFL has not started yet! Please try again with a valid league and season!")
          exit() 
     else:
          pass
elif season == "2020" or season == "2021":
     pass
else:
     print("Oops, you have entered an invalid season. Please try again with a symbol such as '2020' or '2021'.")
     exit()

if sport_league == 'MLB':
     api_key = os.environ.get("api_key")
elif sport_league == 'NBA':
     api_key = os.environ.get("api_key_nba")
elif sport_league == 'NHL': 
     api_key = os.environ.get("api_key_nhl")
elif sport_league == 'NFL':
     api_key = os.environ.get("api_key_nfl")

if season == '2020': 
     request_url = f"https://fly.sportsdata.io/v3/{sport_league}/scores/json/Standings/{season}?key={api_key}"
     response = requests.get(request_url)
     parsed_response = json.loads(response.text)
else:
     request_url = f"https://fly.sportsdata.io/v3/{sport_league}/scores/json/Standings/{season}?key={api_key}"
     response = requests.get(request_url)
     parsed_response = json.loads(response.text)

list_of_team_names = []
for line in parsed_response: 
     if sport_league == 'NFL':
          team_name = line['Name'].split()
          list_of_team_names.append(team_name[-1])
     else:
          list_of_team_names.append(line['Name'])

"""
This is the third major step of the model--selecting a team. The program will access the request_url specific to the 
league and year selected. If selected correctly, the model will complete with a standings displayed. If selected invalid team, 
the model with quit gracefully.
"""
team = input("Please enter the team you would like to view: ")
capitalized_team = team.title()

if capitalized_team in list_of_team_names:
     pass
else: 
     print("Oops, you have entered an invalid team!")
     exit()
     
team_index = list_of_team_names.index(capitalized_team)

if sport_league == 'MLB': 
     league = parsed_response[team_index]["League"]
else:
     league = parsed_response[team_index]["Conference"]
if sport_league == "NFL":
     city = ""
else:
     city = parsed_response[team_index]["City"]
name = parsed_response[team_index]["Name"]
division = parsed_response[team_index]["Division"]
wins = parsed_response[team_index]["Wins"]
losses = parsed_response[team_index]["Losses"]
division_rank = parsed_response[team_index]["DivisionRank"]
if sport_league == 'MLB':
     games_behind = parsed_response[team_index]["GamesBehind"]
elif sport_league == 'NBA': 
     games_behind = parsed_response[team_index]["GamesBack"]
elif sport_league == 'NHL' or sport_league == 'NFL':
     games_behind = ""

named_tuple = time.localtime() 
time_string = time.strftime("%Y-%m-%d, %H:%M:%S", named_tuple)
run_time_date = datetime.datetime.now()
last_refreshed = ("RUN AT: " + run_time_date.strftime("%I:%M %p") + " on " + run_time_date.strftime("%B %d") + ", " + run_time_date.strftime("%Y"))

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "standings.csv")

csv_headers = ["Season", " Team", " Division", " Wins", " Losses", " Division Rank"]


print("-------------------------")
print(f"SEASON: {season}")
if sport_league == 'NFL':
     print(f"SELECTED TEAM: {name}")
else:
     print(f"SELECTED TEAM: {city} {name}")
print("-------------------------")
print("REQUESTING TEAM PERFORMANCE")
print("-------------------------")
print(f"{last_refreshed}")
print(f"LEAGUE: {league}")
print(f"DIVISION: {division}")
print(f"WINS: {wins}")
print(f"LOSSES {losses}")
print(f"DIVISION RANK: {division_rank}")
print(f"GAMES BEHIND: {games_behind}")
print(f"WRITING DATA TO CSV... {csv_file_path}")
print("-------------------------")
print(f"GO {name}!") 
print("-------------------------")


"""
The last part of the model is improting a CSV file that displays the standings in a greater and more detailed 
way for the user to view. This completes the model for the user. 
"""

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames = csv_headers)
    writer.writeheader() # uses fieldnames set above
    for line in parsed_response:
          writer.writerow({
               "Season": line['Season'],
               " Team": line['Name'],
               " Division": line['Division'],
               " Wins": line['Wins'],
               " Losses": line['Losses'], 
               " Division Rank": line['DivisionRank']})