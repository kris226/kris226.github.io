import urllib.request
import bs4
from player_class import Player

def scrape_players():
        
    odpoved = urllib.request.urlopen("https://www.givemesport.com/ballon-dor-power-rankings/")

    polivka = bs4.BeautifulSoup(odpoved, "html.parser")

    tables = polivka.find_all("table")
    rows = tables[0].find_all("tr")



    players : list[Player] = []
    for row in rows[2:]:

        sloupce = row.find_all("td")
        players.append(Player(sloupce[1].p.text, sloupce[2].p.text, sloupce[3].p.text, sloupce[4].p.text))


    return players