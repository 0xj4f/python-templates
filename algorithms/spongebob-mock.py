#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random 

def mock(msg):
    input_text = msg 
    output_text = ""

    for char in input_text: 
        if char.isalpha():
            if random.random() > 0.5: 
                output_text += char.upper()
            else:
                output_text += char.lower()
        else:
            # if not alphabet
            output_text += char

    return output_text

if __name__ == '__main__':
    import sys
    
    phrase = "Something very relevant"
    #response = mock(phrase)
    response = mock("I am bullish")
    print(response)



