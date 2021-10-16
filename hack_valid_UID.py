# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 14:17:10 2021

@author: James Ang
"""

# l = "B1CD102354"
l = "B1CDEF2354"
n = 2
for _ in range(n):
    l = input()

    if len(l) ==10 and sum(c.isalpha() and c.isupper() for c in l) >=2 and sum(c.isdigit() for c in l)>=3 and len(set(l)) == len(l):
        print("Valid")
        
    else:
        print("Invalid")
    
    


    
    
UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
DIGITS    = '0123456789'
ALPHA     = UPPERCASE + LOWERCASE + DIGITS

def valid(uid):
    return (
        two_ucase(uid)        # must contain at least 2 uppercase characters
        and three_digits(uid) # must contain at least 3 digits
        and only_alpha(uid)   # must contain only alphanumeric characters
        and no_repeats(uid)   # no character should repeat
        and ten_chars(uid)    # must be exactly 10 characters long
    )

def two_ucase(uid):
    return sum(1 for i in uid if i in UPPERCASE) >= 2

def three_digits(uid):
    return sum(1 for i in uid if i in DIGITS) >= 3

def only_alpha(uid):
    return all(i in ALPHA for i in uid)

def no_repeats(uid):
    return len(set(uid)) == len(uid)

def ten_chars(uid):
    return len(uid) == 10


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print('Valid' if valid(input()) else 'Invalid')