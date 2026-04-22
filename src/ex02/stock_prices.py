#!/usr/bin/env python3
import sys

def print_stock_price(name):

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

    company_name =  COMPANIES.get(name, False)
    
    if not company_name:
        print("Unknown company")

    else:
        print(STOCKS[company_name])
    


if len(sys.argv) != 2:
    sys.exit(0)
else:
    arg = (sys.argv[1]).capitalize()
    print_stock_price(arg)