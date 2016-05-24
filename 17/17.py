#! /usr/bin/env python3
from __future__ import division
import string

# this problem makes me very sad, there's little elegance to be had here

def num_to_words(number):
    '''convert numbers to english words, max 9999'''
    str_name = ''
    ones_words = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }
    teens_words = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    }
    tens_words = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety',
    }

    # handle thousands place
    if number >= 1000:
        thousands = number // 1000
        str_name += "{} thousand ".format(ones_words[thousands])
        number = number % 1000

    # handle hundreds place
    if number >= 100:
        hundreds = number // 100
        str_name += "{} hundred ".format(ones_words[hundreds])
        number = number % 100
        if number > 0:
            str_name += 'and '

    # special-case 
    if 10 <= number <= 19:
        str_name += teens_words[number]
    else:
        # handle tens place
        if number >= 20:
            tens = number // 10
            str_name += tens_words[tens] + ' '
            number = number % 10
        # handle ones place
        if number > 0:
            str_name += ones_words[number]

    return str_name.strip()

def count_letters(word):
    return len([letter for letter in word if letter in string.ascii_lowercase])

print(sum((count_letters(num_to_words(i)) for i in range(1, 1001))))

