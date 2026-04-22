#!/usr/bin/env python3
import sys

def print_ticker_info(ticker_name):

    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }

    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }

    ticker_price =  STOCKS.get(ticker_name, False)
    company_name = None
    
    for company, ticker in COMPANIES.items():
        if ticker_name == ticker:
            company_name = company
            break
    
    if not ticker_price:
        print("Unknown ticker")
    elif company_name:
        print(f"{company_name} {ticker_price:.2f}")
    
if len(sys.argv) != 2:
    sys.exit(0)
else:
    arg = (sys.argv[1]).upper()
    print_ticker_info(arg)