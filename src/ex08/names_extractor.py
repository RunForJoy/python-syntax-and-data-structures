#!/usr/bin/env python3
import sys

def parse_email(email):
    # name.surname@corp.com
    full_name = email.strip().split('@')[0]
    name = full_name.split('.')[0].capitalize()
    surname = full_name.split('.')[1].capitalize()
    return name, surname



def extract_emails(path):
    try:
        with open(path, encoding='utf-8') as input_file:
            with open('employees.tsv', 'w', encoding='utf-8') as out_file:
                out_file.write("Name\tSurname\tEmail\n") 
                for line in input_file:
                    email = line.strip()
                    name, surname = parse_email(email)
                    out_file.write(f"{name}\t{surname}\t{email}\n")

    except FileNotFoundError:
        raise Exception(f"Файл {path} не найден")


if __name__ == '__main__':    
    if len(sys.argv) != 2:
        raise ValueError("Требуется передать путь к файлу в качестве аргумента.")
    else:
        extract_emails(sys.argv[1])
    