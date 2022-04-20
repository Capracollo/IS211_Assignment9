import requests
from bs4 import BeautifulSoup


def get_prices(url):

    web_page = request.get(url)
    web_data = web_page.text
    soup = BeautifulSoup(web_data, features='lxml')

    rows = soup.find_all('tr', {'class': 'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})

    for row in rows:
        x = row.find_all('td')
        day = str(rows[0].get_text())
        price = str(rows[4].get_text())

        print(f'Date - {day}, price - {price}')


if __name__ == "__main__":
    """Main entry point"""
    url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
    get_prices(url)
