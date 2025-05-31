import os
import urllib.request
import random
import time
from http.client import HTTPResponse

import bs4

odpoved : HTTPResponse = urllib.request.urlopen("https://www.givemesport.com/ballon-dor-power-rankings/")

polivka = bs4.BeautifulSoup(odpoved, "html.parser")

print(polivka.find("p").text)


def clear():
    os.system("cls")

clear()





tables = polivka.find_all("table")
rows = tables[0].find_all("tr")
# print(tables[0])

print(20*"-")

for row in rows:
    print(row)
    print(20*"-")



print(30*"-")
sloupce = rows[3].find_all("td")
for s in sloupce:
    print(s.p.text)
print(30*"-")






class Player:
    def __init__(self, name, team, nationality, position):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.position = position


    def __repr__(self):
        return self.name


    def is_from_nationality(self, country):
        if self.nationality == country:
            return True
        else:
            return False
        

    def is_from_team(self, team):
        if self.team == team:
            return True
        else:
            return False


    def is_from_position(self, position):
            
            if self.position == position:
                return True
            else:
                return False





print(30*"-")


players : list[Player] = []
for row in rows[2:]:

    sloupce = row.find_all("td")
    players.append(Player(sloupce[1].p.text, sloupce[2].p.text, sloupce[3].p.text, sloupce[4].p.text))

    

print(players)



clear()


new_players = []




def Game_nationalityes():
    points = 0
    max_points = len(players)


    for i in range(len(players)):
        clear()
        random_number = random.randint(0, len(players) - 1)
        correct_answer = players[random_number].nationality.lower()
        if input(f"Hello! Which country is {players[random_number]} from? \n").lower() == correct_answer:
            print("Thats correct!!!")
            time.sleep(3)
            points += 1
        else:
            print(f"stupid idiot... Its {correct_answer}")
            time.sleep(3)

        players.pop(random_number)


    print(f"You got {points} points out of {max_points}") 

def Game_Teams():
    points = 0
    max_points = len(players)

    for i in range(len(players)):
        clear()
        random_number = random.randint(0, len(players))
        correct_answer = players[random_number].team.lower()
        if input(f"Hello! Which team is {players[random_number]} from? \n").lower() == correct_answer:
            print("Thats correct!!!")
            time.sleep(3)
            points += 1
        else:
            print(f"stupid idiot... Its {correct_answer}")
            time.sleep(3)

        players.pop(random_number)


    print(f"You got {points} points out of {max_points}") 


def player_games():


    game_wanted = input("Which game do you want to play? \n 1- Nationality game \n 2- Team game \n")
    if game_wanted == "1":
        Game_nationalityes()

    elif game_wanted == "2":
        Game_Teams()






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
