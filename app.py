from pprint import pprint
from implement_mysql import insert_record
from stock import Stock
from selenium import webdriver
from magicformula import magic_formula_login
from magicformula import find_magicformula_stocks
from gurufocusdetails import get_gurufocus_details
from csvfile import write_to_csv


print("Starting webscraping........")

marketcaps = [50, 100, 250, 500, 750, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
# marketcaps = [50, 100]
stock_tickers = {}
chrome_driver = webdriver.Chrome()
magic_formula_login(chrome_driver)
for marketcap in marketcaps:
    find_magicformula_stocks(chrome_driver, marketcap, stock_tickers)
# stock_tickers = dict(set(stock_tickers))
# stock_tickers.sort()
print(stock_tickers)
chrome_driver.close()
print("Completed MagicFormulaInvesting ........")

magic_stock_list = []
print("Getting Details from GuruFocus ........")
for ticker in stock_tickers:
    print(f"Getting data for {ticker} ........")
    magic_stock = get_gurufocus_details(ticker)
    magic_stock.min_market_cap = stock_tickers[ticker]
    # pprint(vars(magic_stock))
    magic_stock_list.append(magic_stock)

print("Completed GuruFocus ........")

print(f"Total number of stocks {len(magic_stock_list)}")
# write_to_csv(magic_stock_list)

print("Inserting records ........")
insert_record(magic_stock_list)
