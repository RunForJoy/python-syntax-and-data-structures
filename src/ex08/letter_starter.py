#!/usr/bin/env python3
import sys


def check_email(email):
    with open('employees.tsv', encoding='utf-8') as f:
        next(f)  
        for line in f:
            name, surname, email_address = line.strip().split('\t')
            if email_address == email:
                print(f"{name}, добро пожаловать в нашу команду! Мы уверены, что работать вместе с тобой будет очень приятно. Для нас это важно - мы стремимся, чтобы в компании работались именно такие люди.")
                return
    print(f"Email {email} не найден")        
                
            

if __name__ == '__main__':    
    if len(sys.argv) != 2:
        raise ValueError("Требуется передать валидный e-mail адрес в формате: name.surname@corp.com в качестве аргумента.")
    else:
        check_email(sys.argv[1])