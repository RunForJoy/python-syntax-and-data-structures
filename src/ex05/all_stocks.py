#!/usr/bin/env python3
import sys

def print_get_stocks():
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

    if len(sys.argv) != 2:
        return

    raw_input = sys.argv[1].split(",")
    cleaned_input = [word.strip() for word in raw_input]
    
    if any([word=="" for word in cleaned_input]):
        return
        
    for request in cleaned_input:
        if request.capitalize() in COMPANIES:
            company = request.capitalize()
            ticker = COMPANIES[company]
            print(f"{company} stock price is {STOCKS[ticker]:.2f}")
        elif request.upper() in STOCKS:
            ticker = request.upper()
            for company_name, ticker_name in COMPANIES.items():
                if ticker == ticker_name:
                    company = company_name
                    print(f"{ticker} is a ticker symbol for {company}")
                    break
        else:
            print(f"{request} is an unknown company or an unknown ticker symbol")
            

if __name__ == '__main__':    
    print_get_stocks()