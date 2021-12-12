from bs4 import BeautifulSoup
import requests
from stock import Stock
from pprint import pprint


def get_gurufocus_details(ticker):
    magic_stock = Stock()
    html_text = requests.get(f'https://www.gurufocus.com/stock/{ticker}/summary').text
    soup = BeautifulSoup(html_text, 'html.parser')
    magic_stock.ticker = ticker

    h1 = soup.find("h1").text
    company_name = h1.split("$")[0].strip()
    price = h1.split("$")[1].split()[0].strip()
    magic_stock.company = company_name


    div = soup.find("div", {"id": "financial-strength"})
    table = div.find("table", {"class": "stock-indicator-table"})
    a_tags = table.findAll('a')
    for a_tag in a_tags:
        if a_tag.text.find("Cash-To-Debt") > -1:
            magic_stock.cash_to_debt =  a_tag.find_parent().find_next_sibling('td').text
        if a_tag.text.find("Debt-to-Equity") > -1:
            magic_stock.debt_to_equity =  a_tag.find_parent().find_next_sibling('td').text
        if a_tag.text.find("Interest Coverage") > -1:
            magic_stock.interest_coverage =  a_tag.find_parent().find_next_sibling('td').text
        if a_tag.text.find("Piotroski F-Score") > -1:
            magic_stock.piotroski_score = a_tag.find_parent().find_next_sibling('td').text

    div = soup.find("div", {"id": "profitability"})
    table = div.find("table", {"class": "stock-indicator-table"})
    a_tags = table.findAll('a')
    for a_tag in a_tags:
        if a_tag.text.find("Operating Margin %") > -1:
            magic_stock.operating_margin = a_tag.find_parent().find_next_sibling('td').text
        if a_tag.text.find("Net Margin %") > -1:
            magic_stock.net_margin = a_tag.find_parent().find_next_sibling('td').text
        if a_tag.text.find("ROE %") > -1:
            magic_stock.return_on_equity = a_tag.find_parent().find_next_sibling('td').text
        if a_tag.text.find("ROA %") > -1:
            magic_stock.return_on_asset = a_tag.find_parent().find_next_sibling('td').text
        if a_tag.text.find("ROC (Joel Greenblatt) %") > -1:
            magic_stock.roc_greenblatt = a_tag.find_parent().find_next_sibling('td').text
        if a_tag.text.find("3-Year Revenue Growth Rate") > -1:
            magic_stock.revenue_growth_3_year = a_tag.find_parent().find_next_sibling('td').text
        if a_tag.text.find("3-Year EPS without NRI Growth Rate") > -1:
            magic_stock.eps_growth_3_year = a_tag.find_parent().find_next_sibling('td').text

    div = soup.find("div", {"id": "ratios"})
    table = div.find("table", {"class": "stock-indicator-table"})
    a_tags = table.findAll('a')
    for a_tag in a_tags:
        if a_tag.text.find("PE Ratio") > -1:
            magic_stock.price_to_earnings = a_tag.find_parent().find_next_sibling('td').text
        if a_tag.text.find("PB Ratio") > -1:
            magic_stock.price_to_book = a_tag.find_parent().find_next_sibling('td').text
        if a_tag.text.find("Price-to-Owner-Earnings") > -1:
            magic_stock.price_to_owner_earnings = a_tag.find_parent().find_next_sibling('td').text
        if a_tag.text.find("Price-to-Operating-Cash-Flow") > -1:
            magic_stock.price_to_operating_cashflow = a_tag.find_parent().find_next_sibling('td').text
        if a_tag.text.find("Price-to-Free-Cash-Flow") > -1:
            magic_stock.price_to_free_cashflow = a_tag.find_parent().find_next_sibling('td').text

    div = soup.find("div", {"id": "dividend"})
    table = div.find("table", {"class": "stock-indicator-table"})
    a_tags = table.findAll('a')
    for a_tag in a_tags:
        if a_tag.text.find("Dividend Yield %") > -1:
            magic_stock.dividend_yield = a_tag.find_parent().find_next_sibling('td').text
        if a_tag.text.find("Dividend Payout Ratio") > -1:
            magic_stock.dividend_payout_ratio = a_tag.find_parent().find_next_sibling('td').text
        if a_tag.text.find("3-Year Dividend Growth Rate") > -1:
            magic_stock.dividend_growth_3_year = a_tag.find_parent().find_next_sibling('td').text
        if a_tag.text.find("3-Year Average Share Buyback Ratio") > -1:
            magic_stock.avg_share_buyback_ratio_3_year = a_tag.find_parent().find_next_sibling('td').text
    div = soup.find("div", {"id": "valuation"})
    table = div.find("table", {"class": "stock-indicator-table"})
    a_tags = table.findAll('a')
    for a_tag in a_tags:
        if a_tag.text.find("Earnings Yield (Greenblatt) %") > -1:
            magic_stock.earnings_yield_greenblatt = float(a_tag.find_parent().find_next_sibling('td').text.strip())

    return magic_stock


# x = get_gurufocus_details('MO')
# pprint(vars(x))












