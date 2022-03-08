import inline
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# %matplotlib inline

import datetime as dt

import time

import yfinance as yf


# YFinance
def get_info_on_stock(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="max")["Close"]
    
#     print(stock.info)
#     print(hist.head())
#     print(stock.financials)
#     print(stock.institutional_holders)
#     print(stock.balance_sheet)
#     print(stock.cashflow)
#     print(stock.earnings)
    print(stock.recommendations)

    
# Calling stock
get_info_on_stock("BHEL.BO")


# Holds Stocks Not Downloaded..
stocks_not_downloaded = []
missing_stocks = []

# Get Stock Tickers..
get_data_from_csv = []
path = r"C:/Users/AYeddula/OneDrive - DXC Production/Desktop/Pythonlang/Python Stocks Data/Bombay.csv"
tickers = get_data_from_csv(path, "Ticker")
tickers

# Function That Saves Stock Data To Csv Files..
def save_to_csv_from_yahoo(folder, ticker):
    stock = yf.Ticker(ticker)
    try:
        print("Get Dat fOR : ", ticker)
        df = stock.history(period="max")["Close"]
        time.sleep(2)
        if df.empty:
            stocks_not_downloaded.append(ticker)
        the_file = folder + ticker.replace(".", "_") + '.csv'
        print(the_file, "Saved")
        df.to_csv(the_file)
    except Exception as ex:
        stocks_not_downloaded.append(ticker)
        print("Couldn't Get Data for :", ticker)
        
        
#         Get 5 years of data for 1 st 20 stocks
        folder = "C:/Users/AYeddula/OneDrive - DXC Production/Desktop/Pythonlang/Python Stocks Data/Bombay.csv"
        for x in range(20):
            save_to_csv_from_yahoo(folder, ticker[x])
        print("Finished")
