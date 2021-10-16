# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 16:22:32 2021

@author: James Ang
"""

from itertools import groupby
n = 6

# cc_num = "5122-3267-8912-3456"
cc_num = "61234-567-8912-3456"
DIGITS = "0123456789-"

def startwith(cc_num):
    return cc_num.startswith("4") or cc_num.startswith("5") or cc_num.startswith("6")

def have16(cc_num):
    return sum([1 for c in cc_num if c.isdigit()]) == 16


def isdigit09(cc_num):
    return all([i in DIGITS for i in cc_num])

def nofour_repeated(cc_num):
    
    cc_digit = "".join([i for i in cc_num if i in DIGITS[:-1]])
    a = [[k, len(list(g))] for k, g in groupby(cc_digit) if k in DIGITS[:-1]]
    
    return all(i[1] < 4 for i in a)

def equalgroup(cc_num):
    if "-" in cc_num:
        c = cc_num.split("-")
    else:
        c = cc_num
    return all([len(i)==4 for i in c]) if "-" in cc_num else True

def valid(cc_num):
    return (startwith(cc_num) and
            have16(cc_num) and
            isdigit09(cc_num) and 
            nofour_repeated(cc_num) and 
            equalgroup(cc_num))

print("Valid" if valid(cc_num) else "Invalid")