import json
import os
import requests
from dotenv import load_dotenv 
#import pandas as pd    #most likely use 
#from datetime import datetime  #most likely use 

load_dotenv()


#INFO INPUTS
#worked with Nolan Matsko and Annabelle Zebrowski 
#checking if ticker has a valid number of characters


api_key = os.environ.get("api_key") 
request_url = f"https://fly.sportsdata.io/v3/mlb/scores/json/Standings/2021?key=5df11bf8ab924b3f8daa67c66e4e617c"
response = requests.get(request_url)
#request_url = f"https://fly.sportsdata.io/v3/mlb/scores/json/Standings/{season}?key={api_key}"

#print(type(response))
#print(response.status_code)
#print(response.text)
#
#
parsed_response = json.loads(response.text)

quit()
#set up API_KEY and possibly default settings

league = os.getenv("league", default="AL")
division = os.getenv("division", default="East")
team = os.getenv("team", default="Baltimore Orioles")
app_env = os.getenv("APP_ENV", default="development")




season = input("Please enter the season you would like to view the MLB standings: ")

if len(season) == 4: 
    pass
else: 
    print("Oops, you have entered an invalid season. Please try again with a symbol such as '2019'.")
    exit()

#check if season has a year

#helped by olisteadman https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number

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
