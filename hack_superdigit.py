# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 00:25:34 2021

@author: James Ang
"""



def superDigit(n, k):
    # Write your code here
    
    num = n*3
    
    num_list = [int(x) for x in num]
    
    while len(num_list) != 1:
        total = sum(num_list)
        num_list = [int(x) for x in str(total)]
    
    
    return num_list[0]


def superDigit1(n,k): # USE THIS ONE
    
    if k == len(n) == 1:
        return int(n)
    # else:
    #     print('nay')
    
    res = 0
    
    for i in n:
        res += int(i)
        
    return superDigit1(str(res*k),1)

if __name__ == '__main__':
    n = '148'
    k = 2
    print(superDigit1(n,k))