# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 12:01:28 2021

@author: James Ang
"""

def cookies(k, A):
    # Write your code here
    print(k)
    print(n)
    j = 0
    
    if sum(A) < k:
        return -1
    
    
    A.sort()
    # A = [number for number in A if number < k]
    # while not all([i>k for i in A]):
    while A[0] <k:
        
        #if A[0] > k:
         #   A = A[1:]
        # temp = A[0] + 2*A[1]
        f = A.pop(0)
        s = A.pop(0)
        A.insert(0,f*2*s)
        A.sort()
        j +=1
    
    
    return j


import heapq

def cookies1(k, A): # other people's solution
    heapq.heapify(A)
    
    ops = 0
    while True:
        f = heapq.heappop(A)
                
        if f >= k:
            return ops
        
        if len(A) == 0:
            return -1
        
        s = heapq.heappop(A)
        n = f + 2*s
        heapq.heappush(A, n)
        
        ops += 1

def cookies2(k, A):
    # Write your code here
    #print(k)
    #print(n)
    ops = 0
    
    if sum(A) < k or len(A)==0:
        return -1
    A.sort()
    
    f = A.pop(0)
    s = A.pop(0)
    
    if f> k:
        return ops

    
    while not all([i>k for i in A]):
        A.sort()
        #temp = A[0] + 2*A[1]
        f = A.pop(0)
        s = A.pop(0)
        A.insert(0,f + 2*s)
        ops +=1
        
    
    return ops

import bisect
def cookies3(k, A):
    # Write your code here
    #print(k)
    #print(n)
    ops = 0

    while True:
        f = A.pop(0)
        if f >=k:
            return ops
        
        if len(A) == 0:
            return -1
        

        
        
        s = A.pop(0)
        bisect.insort(A,f+2*s)
        ops +=1

    
    #return ops


if __name__ == '__main__':
    
    n = 3#6
    k = 10#7
    A = [1,1,1]#[1, 2, 3, 9, 10, 12]
    
    result = cookies3(k, A)
    print(result)