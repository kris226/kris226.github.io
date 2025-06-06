import os
import random
import time
from player_class import Player
from scraping_module import scrape_players






def clear():
    os.system("cls")

clear()






players : list[Player] = scrape_players()


print(players)



clear()


new_players = []




def ask_nationality(nationality):
    global players
    new_players = []
    input_lol = input(f"is your player from {nationality}?").lower()

    clear()


    if input_lol == "no":
        



        for player in players:
            if player.is_from_nationality(nationality) == False:
                new_players.append(player)


    elif input_lol== "yes":
        for player in players:
            if player.is_from_nationality(nationality) == True:
                new_players.append(player)

    players = new_players





def ask_team(team):
    global players
    new_players = []
    input_lol = input(f"does your player play in {team}?").lower()

    clear()


    if input_lol == "no":
        
        for player in players:
            if player.is_from_team(team) == False:
                new_players.append(player)


    elif input_lol== "yes":
        for player in players:
            if player.is_from_team(team) == True:
                new_players.append(player)

    players = new_players



def ask_position(position):
    global players
    new_players = []
    input_lol = input(f"is your player a {position}?").lower()

    clear()


    if input_lol == "no":
        
        for player in players:
            if player.is_from_position(position) == False:
                new_players.append(player)


    elif input_lol== "yes":
        for player in players:
            if player.is_from_position(position) == True:
                new_players.append(player)

    players = new_players







def print_player_names():
    for player in players:
        print(player.name)
    print(len(players))








def find_most_helpfull():
    global best_kriterium, best_name, best_number


    nationalities = []
    teams = []
    positions = []

    
    best_number = 0
    best_name = None
    best_kriterium = None

    for player in players:
        nationalities.append(player.nationality)
        teams.append(player.team)
        positions.append(player.position)



    for i in range(len(nationalities)):
        if nationalities.count(nationalities[i]) > best_number and nationalities.count(nationalities[i]) < len(nationalities):
            best_number = nationalities.count(nationalities[i])
            best_name = nationalities[i]
            best_kriterium = "nationality"



    for i in range(len(teams)):
        if teams.count(teams[i]) > best_number and teams.count(teams[i]) < len(teams):
            best_number = teams.count(teams[i])
            best_name = teams[i]
            best_kriterium = "team"


    for i in range(len(positions)):
        if positions.count(positions[i]) > best_number and positions.count(positions[i]) < len(positions):
            best_number = positions.count(positions[i])
            best_name = positions[i]
            best_kriterium = "position"





clear()

# find_most_helpfull()

def ask_best():

    find_most_helpfull()

    if best_kriterium == "nationality":
        ask_nationality(best_name)


    if best_kriterium == "team":
        ask_team(best_name)


    if best_kriterium == "position":
        ask_position(best_name)



for i in range(100):
    if len(players) == 1:
        if input(f"Is your player {players[0].name}?") == "yes":
            clear()
            print("Lets goooo")
            exit()

    ask_best()






