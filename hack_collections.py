# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 16:36:03 2021

@author: James Ang
"""

from collections import Counter

n_types = "10"
# print(n_types)

s = "2 3 4 5 6 8 7 6 5 18"

sizes = list(map(int, s.split()))

#sizes = input().split()
# print(f"sizes: {list(sizes)}")

count_dict = Counter(sizes)
# print(count_dict)


#keys = count_dict.keys()
#values = count_dict.values()

# print(keys)

# for i, j in count_dict.items():
#     print(i,j)


n_cust = 6

l = ["6 55", "6 45", "6 55", "4 40", "18 60", "10 50"]
#print(n_cust, type(n_cust))

total = 0

for j in l:
    s,price = list(map(int,j.split()))
    
    if count_dict[s]:
        count_dict[s] -=1
        total += price
print(total)
        
        # print(s,price)
        # print(type(s),type(price))
"""
Answer in hackerank
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n_types = input()
# print(n_types)

#s = "2 3 4 5 6 8 7 6 5 18"

sizes = list(map(int, input().split()))

#sizes = input().split()
# print(f"sizes: {list(sizes)}")

count_dict = Counter(sizes)
# print(count_dict)


#keys = count_dict.keys()
#values = count_dict.values()

# print(keys)

# for i, j in count_dict.items():
#     print(i,j)


n_cust = int(input())

#l = ["6 55", "6 45", "6 55", "4 40", "18 60", "10 50"]
#print(n_cust, type(n_cust))

total = 0

for _ in range(n_cust):
    #s,price = list(map(int,j.split()))
    s,price = list(map(int,input().split()))
    
    if count_dict[s]:
        count_dict[s] -=1
        total += price
print(total)
"""