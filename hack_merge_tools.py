# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 09:47:57 2021

@author: James Ang
"""

def merge_the_tools(string, k):
    # your code goes here
    # s = [''.join(set(string[i:i + k])) for i in range(0, len(string),k)]
    
    for i in range(0, len(string),k):
        
        # print(i)
        l = []
        
        for j in string[i:i + k]:
            # print(j)
            if j not in l:
                l.append(j)
            
        word = "".join(l)
        
        print(word)
        
        
        # print(string[i:i + k])
        
    # continue here
    # for word in s:
    #     print ("".join(word))

if __name__ == '__main__':
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)