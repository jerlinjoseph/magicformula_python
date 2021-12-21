import time
import os
from dotenv import load_dotenv
load_dotenv()
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def magic_formula_parse_html(marketcap, html_text, tickers):
    soup = BeautifulSoup(html_text, 'html.parser')
    div = soup.find("div", {"id": 'tableform'})
    #select all the 2nd td's
    tds = div.select('table.screeningdata > tbody > tr > td:nth-child(2)')
    print(f"Stocks with minimum market cap of {marketcap}")
    for td in tds:
        #print(td.text)
        #tickers.append(td.text)
        if td.text not in tickers:
            tickers[td.text] = marketcap


def magic_formula_login(driver):
    user_name = os.environ.get('MAGIC_USER')
    password = os.environ.get('MAGIC_PASSWORD')
    print(user_name)
    print(password)
    driver.get('https://www.magicformulainvesting.com/Account/LogOn')
    driver.find_element(By.ID, "Email").send_keys(user_name)
    driver.find_element(By.ID, "Password").send_keys(password)
    driver.find_element(By.ID, "login").click()


# find tickers for a specific market cap
def find_magicformula_stocks(driver, marketcap, tickers):
   minimumMarketCap = driver.find_element(By.ID, "MinimumMarketCap")
   minimumMarketCap.clear()
   minimumMarketCap.send_keys(marketcap)
   radioButton = driver.find_element(By.XPATH,
                                  "/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[4]/td[2]/table/tbody/tr[1]/td[3]/span/input")
   radioButton.click()
   driver.find_element(By.ID, "stocks").click()
   time.sleep(2)
   html = driver.page_source
   magic_formula_parse_html(marketcap, html, tickers)


# marketcaps = [50, 250, 500, 1000, 2500, 5000]
# stock_tickers = []
# chrome_driver = webdriver.Chrome()
# magic_formula_login(chrome_driver)
# for marketcap in marketcaps:
#     find_magicformula_stocks(chrome_driver, marketcap, stock_tickers)
# stock_tickers = list(set(stock_tickers))
# stock_tickers.sort()
# print(stock_tickers)
# chrome_driver.close()


