#!/usr/bin/env python3
import sys

def check_input():
    if len(sys.argv) != 2:
        sys.exit(0)
    else:
        raw_input = sys.argv[1].split(",")
        cleaned_input = [word.strip() for word in raw_input]
        if not all([len[word] for word in cleaned_input]):
            sys.exit(0)
        

def stocks():
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

   


        

     
print_get_stocks()