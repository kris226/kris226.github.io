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
    def __init__(self, name, team, nationallity, position):
        self.name = name
        self.team = team
        self.nationallity = nationallity
        self.position = position


    def __repr__(self):
        return self.name


    def is_from_country(self, country):
        
        if self.name == "Jude Bellingham":
            print("belingham was at 1")
        
        print("got to 2")
        
        
        if self.nationallity == country:
            print("got to 3")
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







def Game_nationallityes():
    points = 0
    max_points = len(players)


    for i in range(len(players)):
        clear()
        random_number = random.randint(0, len(players) - 1)
        correct_answer = players[random_number].nationallity.lower()
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


    game_wanted = input("Which game do you want to play? \n 1- Nationallity game \n 2- Team game \n")
    if game_wanted == "1":
        Game_nationallityes()

    elif game_wanted == "2":
        Game_Teams()



if input("is your player english?") == "no":
    print("got to 1")
    for player in players:
        if player.is_from_country("England") == True:
            print(f"removing {player.name}")
            players.remove(player)


elif input("is your player english?") == "yes":
    for player in players:
        if player.is_from_country("England") == False:
            print(f"removing {player.name}")
            players.remove(player)


for player in players:
    
    print(player.name)

print(len(players))

