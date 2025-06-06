import os
import urllib.request
import random
import time
from player_class import Player
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







print(30*"-")


players : list[Player] = []
for row in rows[2:]:

    sloupce = row.find_all("td")
    players.append(Player(sloupce[1].p.text, sloupce[2].p.text, sloupce[3].p.text, sloupce[4].p.text))

    

print(players)



clear()


def Game_Both(atribute, extr):
    points = 0
    max_points = len(players)

    for i in range(len(players)):
        clear()
        random_number = random.randint(0, len(players)-1)
        correct_answer = extr(players[random_number]).lower()
        if input(f"Hello! What is the {atribute} of {players[random_number]}? \n").lower() == correct_answer:
            print("Thats correct!!!")
            time.sleep(3)
            points += 1
        else:
            print(f"stupid idiot... Its {correct_answer}")
            time.sleep(3)

        players.pop(random_number)


    print(f"You got {points} points out of {max_points}")




def nationality_extr(player : Player):
    return player.nationality



def team_extr(player : Player):
    return player.team


def position_extr(player : Player):
    return player.position




game_wanted = input("Which game do you want to play? \n 1- Nationallity game \n 2- Team game \n 3- Position game \n")
if game_wanted == "1":
    Game_Both("country", nationality_extr)

elif game_wanted == "2":
    Game_Both("team", team_extr)


elif game_wanted == "3":
    Game_Both("position", position_extr)