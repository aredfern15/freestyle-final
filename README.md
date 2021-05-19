#  Freestyle Final 

## Description 
add description of service here 

## Installation

Fork [this repo](https://github.com/agz9/freestyle-final), then clone or download the forked repo onto your local computer (for example to the Desktop), then navigate there from the command-line:

```sh
cd ~/Desktop/freestyle-final/
```

Use Anaconda to create and activate a new virtual environment, perhaps called "freestyle-env":

```sh
conda create -n freestyle-env python=3.8
conda activate freestyle-env
```

Then, within an active virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```
### Enviroment Variable - API Keys

You will need 4 API Keys to run the program. Go to [AlphaVantage API](https://www.alphavantage.co) and sign up for an API key. You should then set an environment variable called `API_KEY_LEAGUE` in your local repo in a file named ".env".

```
API_KEY_MLB="<Your MLB API Key>"
API_KEY_NFL="<Your NFL API Key>"
API_KEY_NHL="<Your NHL API Key>"
API_KEY_NBA="<Your NBA API Key>"
```

## Instructions

Run the program from the command-line:

```sh
python -m app/League_Standings.py
```

## Running the Program

Upon running the program, you will be asked to input which sports league you would like to see: MLB, NFL, NHL, or NBA. After this selection, the user will enter for which year they would like to see the information - 2020 or 2021 season. Lastly, the user will be asked for a specific team to view from that league. 

At any point, if the user input is not found within the data, the program will exit gracefully, prompting the user to run the program again from their command line or terminal. 

Upon completion, the user will receive a list of updated statistics for the team they chose, as well as a CSV with the information for the chosen season and league, for their further exploration. 

Enjoy the program, and GO "ENTER USER FAVORITE TEAM"! 

## Future Usage

Be on the lookout -- updates coming soon! Next up, you'll be able to view stats from other sports and years as well! 