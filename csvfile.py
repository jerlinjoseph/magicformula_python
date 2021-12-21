import csv
from pprint import pprint

import csvfile
from gurufocusdetails import get_gurufocus_details


def write_to_csv(magic_stock_list):
    global writer
    # field names
    fields = ['Ticker', 'Company', 'Min Mkt Cap', 'Earnings Yield', 'ROC Greenblatt',
              'Interest Coverage', 'Piotroski Score', 'Cash to Debt', 'Debt to Equity',
              'Operating Margin', 'Net Margin', 'ROE', 'ROA', '3 year revenue growth',
              '3 year eps growth', 'P/E', 'P/B', 'P/OE', 'P/FCF', 'P/OCF', 'Dividend Yield',
              'Payout Ratio', '3 year dividend growth', '3 year avg share buyback']
    # name of csv file
    filename = "MagicFormulaStocks.csv"
    try:
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
            for item in magic_stock_list:
                writer.writerow([item.ticker,
                                 item.company,
                                 item.min_market_cap,
                                 item.earnings_yield_greenblatt,
                                 item.roc_greenblatt,
                                 item.interest_coverage,
                                 item.piotroski_score,
                                 item.cash_to_debt,
                                 item.debt_to_equity,
                                 item.operating_margin,
                                 item.net_margin,
                                 item.return_on_equity,
                                 item.return_on_asset,
                                 item.revenue_growth_3_year,
                                 item.eps_growth_3_year,
                                 item.price_to_earnings,
                                 item.price_to_book,
                                 item.price_to_owner_earnings,
                                 item.price_to_free_cashflow,
                                 item.price_to_operating_cashflow,
                                 item.dividend_yield,
                                 item.dividend_payout_ratio,
                                 item.dividend_growth_3_year,
                                 item.avg_share_buyback_ratio_3_year,
                                 item.min_market_cap])
    except BaseException as e:
        print(e)
    else:
        print('Data has been loaded successfully !')


# stock_tickers = ['MO', 'BIIB', 'AZO']
# magic_stock_list = []
# print("Getting Details from GuruFocus ........")
# for ticker in stock_tickers:
#     print(f"Getting data for {ticker} ........")
#     magic_stock = get_gurufocus_details(ticker)
#     pprint(vars(magic_stock))
#     magic_stock_list.append(magic_stock)
#
# print("Completed GuruFocus ........")
#
# print(len(magic_stock_list))
# write_to_csv(magic_stock_list)
