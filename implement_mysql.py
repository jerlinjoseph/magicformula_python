from pprint import pprint

import mysql.connector


def create_table():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="jerlin",
        database="magicformula")
    mycursor = db.cursor()
    # mycursor.execute("DROP Table stocks")
    # db.commit()
    mycursor.execute(""" CREATE TABLE stocks
            (ticker VARCHAR(10),
            company VARCHAR(100),
            earnings_yield_greenblatt FLOAT(7,2),
            roc_greenblatt FLOAT(10,2),
            interest_coverage FLOAT(7,2),
            piotroski_score INTEGER,
            cash_to_debt FLOAT(7,2),
            debt_to_equity FLOAT(7,2),
            operating_margin FLOAT(7,2),
            net_margin FLOAT(7,2),
            return_on_equity FLOAT(7,2),
            return_on_asset FLOAT(7,2),
            revenue_growth_3_year FLOAT(7,2),
            eps_growth_3_year FLOAT(7,2),
            price_to_earnings FLOAT(7,2),
            price_to_book FLOAT(7,2),
            price_to_owner_earnings FLOAT(7,2),
            price_to_free_cashflow FLOAT(7,2),
            price_to_operating_cashflow FLOAT(7,2),
            dividend_yield FLOAT(7,2),
            dividend_payout_ratio FLOAT(7,2),
            dividend_growth_3_year FLOAT(7,2),
            avg_share_buyback_ratio_3_year FLOAT(7,2),
            min_market_cap INTEGER) """)

    db.commit()


def insert_record(stocks):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="jerlin",
        database="magicformula")
    mycursor = db.cursor()
    delete_query = "delete from stocks"
    mycursor.execute(delete_query)
    for stock in stocks:
        pprint(vars(stock))
        query = """ INSERT INTO stocks(
                            ticker ,
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
                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                              %s, %s) """
        record = (stock.ticker, stock.company, stock.earnings_yield_greenblatt, stock.roc_greenblatt, stock.interest_coverage,
                  stock.piotroski_score, stock.cash_to_debt, stock.debt_to_equity, stock.operating_margin, stock.net_margin,
                  stock.return_on_equity, stock.return_on_asset, stock.revenue_growth_3_year, stock.eps_growth_3_year,
                  stock.price_to_earnings, stock.price_to_book, stock.price_to_owner_earnings, stock.price_to_free_cashflow,
                  stock.price_to_operating_cashflow, stock.dividend_yield, stock.dividend_payout_ratio, stock.dividend_growth_3_year,
                  stock.avg_share_buyback_ratio_3_year, stock.min_market_cap)

        mycursor.execute(query, record)

    db.commit()
    mycursor.close()


# create_table()