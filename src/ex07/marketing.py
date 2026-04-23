#!/usr/bin/env python3

import sys

def get_list_for_call_center(clients, recipients):
    return list(set(clients).difference(set(recipients)))

def get_emails_of_potential_clients(participants, clients):
    return list(set(participants).difference(set(clients)))

def get_emails_for_loyalty_program(clients, participants):
    return list(set(clients).difference(set(participants)))


def get_info_from_db(command):
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
    'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
    'elon@paypal.com', 'jessica@gmail.com']
    
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']

    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    if command == 'call_center':
        target_emails = get_list_for_call_center(clients, recipients)
        print(target_emails)
    elif command == 'potential_clients':
        target_emails = get_emails_of_potential_clients(participants, clients)
        print(target_emails)
    elif command == 'loyalty_program':
        target_emails = get_emails_for_loyalty_program(clients, participants)
        print(target_emails)
            

if __name__ == '__main__':    
    if len(sys.argv) != 2:
        raise ValueError("Требуется один аргумент командной строки")
    else:
        command_list = ['call_center', 'potential_clients', 'loyalty_program']
        arg = sys.argv[1].lower()
        if arg not in command_list:
            raise ValueError(f"Неверный аргумент '{arg}'. Используйте: call_center, potential_clients или loyalty_program")
        else:
            get_info_from_db(arg)
    