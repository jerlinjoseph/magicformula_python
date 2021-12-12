class Stock:
    def __init__(self, ticker = None, company = None, cash_to_debt = None, debt_to_equity = None, interest_coverage = None,
                 piotroski_score = None, operating_margin = None, net_margin = None, return_on_equity = None,
                 return_on_asset = None, roc_greenblatt = None, revenue_growth_3_year = None, eps_growth_3_year = None,
                 price_to_earnings = None, price_to_book = None, price_to_owner_earnings = None,
                 price_to_free_cashflow = None, price_to_operating_cashflow = None, dividend_yield = None,
                 dividend_payout_ratio = None, dividend_growth_3_year = None, earnings_yield_greenblatt = None,
                 avg_share_buyback_ratio_3_year = None, min_market_cap = None):

        self.ticker = ticker
        self.company = company
        self.cash_to_debt = cash_to_debt
        self.debt_to_equity = debt_to_equity
        self.interest_coverage = interest_coverage
        self.piotroski_score = piotroski_score
        self.operating_margin = operating_margin
        self.net_margin = net_margin
        self.return_on_equity = return_on_equity
        self.return_on_asset = return_on_asset
        self.roc_greenblatt = roc_greenblatt
        self.revenue_growth_3_year = revenue_growth_3_year
        self.eps_growth_3_year = eps_growth_3_year
        self.price_to_earnings = price_to_earnings
        self.price_to_book = price_to_book
        self.price_to_owner_earnings = price_to_owner_earnings
        self.price_to_free_cashflow = price_to_free_cashflow
        self.price_to_operating_cashflow = price_to_operating_cashflow
        self.dividend_yield = dividend_yield
        self.dividend_payout_ratio = dividend_payout_ratio
        self.dividend_growth_3_year = dividend_growth_3_year
        self.earnings_yield_greenblatt = earnings_yield_greenblatt
        self.avg_share_buyback_ratio_3_year = avg_share_buyback_ratio_3_year
        self.min_market_cap = min_market_cap




