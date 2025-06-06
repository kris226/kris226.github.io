import os

import random
import time
from player_class import Player
from http.client import HTTPResponse
from scraping_module import scrape_players


players = scrape_players()




def clear():
    os.system("cls")






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