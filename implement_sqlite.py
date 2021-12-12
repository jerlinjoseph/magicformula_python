import sqlite3
from pprint import pprint

from stock import Stock


def create_table():
    conn = sqlite3.connect("magic_stocks.db")
    c = conn.cursor()
    c.execute(""" CREATE TABLE stocks
            (ticker text,
            company text,       
            earnings_yield_greenblatt real,
            roc_greenblatt real,
            interest_coverage real,
            piotroski_score integer,
            cash_to_debt real,
            debt_to_equity real,
            operating_margin real,
            net_margin real,
            return_on_equity real,
            return_on_asset real,
            revenue_growth_3_year real,
            eps_growth_3_year real,
            price_to_earnings real,
            price_to_book real,
            price_to_owner_earnings real,
            price_to_free_cashflow real,
            price_to_operating_cashflow real,
            dividend_yield real,
            dividend_payout_ratio real,
            dividend_growth_3_year real,
            avg_share_buyback_ratio_3_year real,
            min_market_cap real) """)

    conn.commit()
    conn.close()


def insert_record(stocks):
    conn = sqlite3.connect("magic_stocks.db")
    conn.set_trace_callback(print)
    c = conn.cursor()
    for stock in stocks:
        pprint(vars(stock))
        c.execute(f""" INSERT INTO stocks
            (ticker ,
            company ,
            earnings_yield_greenblatt ,
            roc_greenblatt ,
            interest_coverage ,
            piotroski_score ,
            cash_to_debt ,
            debt_to_equity ,
            operating_margin ,
            net_margin ,
            return_on_equity ,
            return_on_asset ,
            revenue_growth_3_year ,
            eps_growth_3_year ,
            price_to_earnings ,
            price_to_book ,
            price_to_owner_earnings ,
            price_to_free_cashflow ,
            price_to_operating_cashflow ,
            dividend_yield ,
            dividend_payout_ratio ,
            dividend_growth_3_year ,
            avg_share_buyback_ratio_3_year ,
            min_market_cap )
            VALUES(
                    {stock.ticker},
                    {stock.company},
                    {stock.earnings_yield_greenblatt},
                    {stock.roc_greenblatt},
                    {stock.interest_coverage},
                    {stock.piotroski_score},
                    {stock.cash_to_debt},
                    {stock.debt_to_equity},
                    {stock.operating_margin},
                    {stock.net_margin},
                    {stock.return_on_equity},
                    {stock.return_on_asset},
                    {stock.revenue_growth_3_year},
                    {stock.eps_growth_3_year},
                    {stock.price_to_earnings},
                    {stock.price_to_book},
                    {stock.price_to_owner_earnings},
                    {stock.price_to_free_cashflow},
                    {stock.price_to_operating_cashflow},
                    {stock.dividend_yield},
                    {stock.dividend_payout_ratio},
                    {stock.dividend_growth_3_year},
                    {stock.avg_share_buyback_ratio_3_year},
                    {stock.min_market_cap})
        """)
    conn.commit()
    conn.close()




