from bs4 import BeautifulSoup
from telebot import TeleBot
import requests

bot = TeleBot()

game = input("What game would you like to monitor? ")

price_limit = int(input("What is the highest price limit? "))

search_game_url = f"https://store.steampowered.com/search/?term={game}"

search_response = requests.get(search_game_url)
search_data = search_response.text

search_soup = BeautifulSoup(search_data, "html.parser")

search_link = search_soup.find(name="div", id="search_resultsRows")
game_url = search_link.find(name="a", class_="search_result_row ds_collapse_flag").get("href")

response = requests.get(game_url)
web_data = response.text

web_soup = BeautifulSoup(web_data, "html.parser")
game_price_list = web_soup.find(name="div", class_="game_purchase_price price").get_text().strip().split()
#game_price = int(game_price_list[0].split(",")[0]) - for Norway, will add as try except later
game_price = int(game_price_list[0])

if game_price <= price_limit:
    bot.send_message(f"Check out price for {game}! It's {game_price} RUB! Find it here: {game_url}")
