from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time
from file import save

def scrape(fileName):
    url = 'https://store.steampowered.com/search/?filter=topsellers&os=win'

    gamePriceInfo = []

    p = sync_playwright().start()
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)

    for i in range(10):
        page.keyboard.down('End')
        time.sleep(0.5)

    content = page.content()

    p.stop()

    soup = BeautifulSoup(content, 'html.parser')

    games = soup.find_all('a', class_='search_result_row ds_collapse_flag')

    for game in games:
        title = game.find('span', class_='title').text
        discount = game.find('div', class_='discount_pct')
        price = game.find('div', class_='discount_prices')

        if(discount != None):
            ogprice = price.text.strip().split('C$')[1]
            newprice = price.text.strip().split('C$')[2]
            gamelist = {
                'title': title,
                'discount': discount.text.strip(),
                'ogprice': ogprice,
                'newprice': newprice,
                'link': game.get('href')
            }
            gamePriceInfo.append(gamelist)
    
    save(fileName, gamePriceInfo)
    
    return gamePriceInfo