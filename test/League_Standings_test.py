
from app.League_Standings import valid_leagues, season, list_of_team_names, name, season, valid_seasons, csv_file_path, csv_headers


def test_valid_leagues():
    sport_league = valid_leagues
    assert "MLB" in sport_league
    assert "NBA" in sport_league


def test_list_of_team_names(): 
    name = list_of_team_names
    assert "Red Sox" in name
    assert "Celtics" in name


def test_valid_seasons():
    season = valid_seasons
    assert "2021" in season
    assert "2020" in season


def test_csv_file_path(): 
    csv_headers = csv_file_path
    assert "Season" in csv_headers
    assert "Team" in csv_headers
