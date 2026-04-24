#!/usr/bin/env python3
import sys


def ave_cezar(user_string: str, shift: int) -> str:
    res = ''
    for char in user_string:
        if char.isalpha():
            if char.isupper():
                first_ord = ord('A')
            else:
                first_ord = ord('a')

            delta_point = ord(char) - first_ord
            num = (delta_point + shift) % 26
            char = chr(num + first_ord)
            res += char
        else:
            res += char
    return res


def is_alpha_has_only_latin_letters(user_string: str) -> bool:
    for char in user_string:
        if char.isalpha():
            if 'а' <= char.lower() <= 'я' or char.lower() == 'ё':
            # еще вариант, но не сработает, напр,  с фр.буквами: if not char.isascii():
                return False
    return True


def input_is_valid():
    if len(sys.argv) != 4:
        raise ValueError("Для работы скрипта необходимо передать ровно 3 аргумента вида:\n encode или decode 'LatinStroke' shift. Пример: encode 'I love School' 21")
    elif sys.argv[1] not in ('encode', 'decode'):
        raise ValueError("Не передан валидный режим шифрования/дешифрования")
    elif not sys.argv[3].isdigit():
        raise ValueError("Не передано числовое значение сдвига")
    elif not is_alpha_has_only_latin_letters(sys.argv[2]):
        raise ValueError("The script does not support your language yet.")
    return True
    
 
if __name__ == '__main__':  
    input_is_valid()
       
    if sys.argv[1]=='encode':
        result = ave_cezar(sys.argv[2], int(sys.argv[3]))
    else:
         result = ave_cezar(sys.argv[2], -int(sys.argv[3]))
    print(result)

  
    


   

