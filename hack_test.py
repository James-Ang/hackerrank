# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 19:05:37 2021

@author: James Ang
"""

def minimizeBias(ratings):
    
    tot = []
    ratings.sort()
    for i in range(0,len(ratings),2):
        
        tot.append(ratings[i+1]-ratings[i])
        # print(tot)

    
    return sum(tot)

if __name__ == '__main__':
    ratings = [1, 3, 6, 6]
    
    ratings = minimizeBias(ratings)
    print(ratings)