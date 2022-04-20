import requests
from bs4 import BeautifulSoup



def get_player(url):

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    div_tag = soup.find_all('div', class_='TableBase-overflow')
    trs_tag = div_tag[0].find_all('tr', class_="TableBase-bodyTr")

    counter = 0
    for tr_tag in trs_tag:
        counter += 1
        if counter <= 20:
            td_tag = tr_tag.find_all('td')
            # get the player name
            info = td_tag[0].find_all('span', class_='CellPlayerName--long')
            player_info = info[0].text
            player_split = " ".join(player_info.split())
            player_space = player_split.split(' ')

            team = player_space[-1]
            position = player_space[-2]
            name = player_space[0] + ' ' + player_space[1]

            print("Player Name: " + name)
            print("Player Position: " + position)
            print("Player Team: " + team)

            # get player points scored
            points_td = td[12].text.strip()
            print("Points scored: " + points_td)


if __name__ == "__main__":
    """Main entry point"""
    url = "https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/"
    get_player(url)
