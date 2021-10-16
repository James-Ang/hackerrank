# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 10:59:28 2021

2

1 7

3 7

@author: James Ang
"""
def towerBreakers(n, m):
    # Write your code here
    
    if n%2 ==0 or m==1:
        winner = 2
    else:
        winner = 1
    
    return winner


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)
        print(result)