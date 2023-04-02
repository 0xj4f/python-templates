#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(message):
    cipher = ""
    for letter in message: 
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            cipher += " "

    return cipher

def decrypt(message):
    message += " "
    decipher = ""
    citext = ""
    
    for letter in message:
        if letter != " ":
            i = 0 # Tracks space
            citext += letter  # storing morse code character

        else: # incase of space
            i += 1
            if i == 2: # indicates a new word
                decipher += " " # Add space to seperate words
            else: 
                decipher += list(MORSE_CODE_DICT.keys()) [list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ""
    return decipher

def main(message): 
    result = encrypt(message.upper())
    print( result )
    
    message = result
    result = decrypt(message)
    print( result )

if __name__ == '__main__':
    import sys 
    try:
        message = sys.argv[1]
        main(message)
    except: 
        message = "I love you"
        main(message)






