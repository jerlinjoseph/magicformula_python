from pprint import pprint

from gurufocusdetails import get_gurufocus_details
from implement_sqlite import insert_record

stock_tickers = ['MO']
magic_stock_list = []
print("Getting Details from GuruFocus ........")
for ticker in stock_tickers:
    print(f"Getting data for {ticker} ........")
    magic_stock = get_gurufocus_details(ticker)
    pprint(vars(magic_stock))
    magic_stock_list.append(magic_stock)

print("Completed GuruFocus ........")

print(len(magic_stock_list))
#write_to_csv(magic_stock_list)

print("Inserting records ........")
insert_record(magic_stock_list)