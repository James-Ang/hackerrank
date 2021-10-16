# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:48:56 2021

@author: James Ang
"""

grid = ['ebacd', 'faaaa', 'olmkn', 'trpqs', 'xywuv']

def isInAlphabeticalOrder(word):
    return word==''.join(sorted(word))



def gridChallenge(grid):
    # Write your code here
    g = []
    for i in grid:
        
        sorted_row_list = sorted(i)
        g.append(sorted_row_list)
        
        word = "".join(sorted_row_list)
        # print(word)
        # print("\n")
        
        #print(isInAlphabeticalOrder(word))
        # print(i)
    
    g_transpose = list(map(list, zip(*g)))
    
    verdict = "YES"
    
    for i in g_transpose:
        
        # sorted_row_list = sorted(i)
        word = "".join(i)
        print(word)
        if not isInAlphabeticalOrder(word):
            verdict = "NO"
            break

    
    return verdict

if __name__ == '__main__':
    result = gridChallenge(grid)
    print(result)