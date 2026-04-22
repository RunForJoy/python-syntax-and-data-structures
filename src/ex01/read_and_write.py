#!/usr/bin/env python3

with open('ds.csv', encoding='utf-8') as file:
    for line in file:
        output = ''
        inside_quotes = False   # переменная-флаг, начальное состояние — снаружи кавычек
        
        for char in line:
            
            if char == '"':
                inside_quotes = True   
                output += '"'
            elif char == '"':
                inside_quotes = not inside_quotes  
                output += '"'
                
            elif char == ',':
                if inside_quotes:
                     # внутри кавычек — оставляем запятую
                    output += ','
                else:
                    # снаружи кавычек — заменяем на табуляцию
                    output += '\t'
            else:
                output += char
        print(output)