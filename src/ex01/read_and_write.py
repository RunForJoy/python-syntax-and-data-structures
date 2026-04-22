#!/usr/bin/env python3

with open('ds.csv', encoding='utf-8') as file:
    with open('ds.tsv', 'w', encoding='utf-8') as out_file:
        for line in file:
            inside_quotes = False  
            output = ''
                
            for char in line:
                if char == '"': 
                    inside_quotes = not inside_quotes  
                    output += '"'
                elif char == ',':
                    if inside_quotes:
                        output += ','
                    else:
                        output += '\t'
                else:
                    output += char
            out_file.write(output)