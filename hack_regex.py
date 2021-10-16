# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 20:41:10 2021

https://www.programiz.com/python-programming/regex

@author: James Ang
"""

# regex_integer_in_range = r"_________"	# Do not delete 'r'.
# regex_alternating_repetitive_digit_pair = r"_________"	# Do not delete 'r'.



regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"

import re
P = "110000"

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# tests
re.match(r"^[1-9][0-9]{5}$", "410003")
