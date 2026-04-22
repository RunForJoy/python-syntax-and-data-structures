#!/usr/bin/env python3

def convert_to_dict():
    list_of_tuples = [
    ('Russia', '25'),
    ('France', '132'),
    ('Germany', '132'),
    ('Spain', '178'),
    ('Italy', '162'),
    ('Portugal', '17'),
    ('Finland', '3'),
    ('Hungary', '2'),
    ('The Netherlands', '28'),
    ('The USA', '610'),
    ('The United Kingdom', '95'),
    ('China', '83'),
    ('Iran', '76'),
    ('Turkey', '65'),
    ('Belgium', '34'),
    ('Canada', '28'),
    ('Switzerland', '26'),
    ('Brazil', '25'),
    ('Austria', '14'),
    ('Israel', '12')
    ]
    
    #dct = {v: k for k, v in list_of_tuples}
    #for k, v in dct.items():
    #    print(f"{k} : {v}")

    dct_of_countries = {}

    for country, num in list_of_tuples:
        dct_of_countries.setdefault(num, []).append(country)


    for num, lst_of_countries in dct_of_countries.items():
        for country in lst_of_countries:
            print(f"'{num}' : '{country}'")



convert_to_dict()