# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 18:06:14 2021

@author: James Ang
"""

def minimumBribes(q):
    # Write your code here
    tot = 0
    flag = 0
    
    for i, val in enumerate(q):
        
        #print(i,val)
        if val - i -1 ==1:
            tot += 1
            
        elif val - i -1 ==2:
            tot += 2
            
        elif val - i -1 >2:
            print("Too chaotic")
            # flag = 1
            return
        else:
            pass
    # if flag == 0:
    print(tot)

def minimumBribes1(q): # Given Answer!
    total_bribes = 0
    i = len(q) - 1
    while i >= 0:
        diff = q[i] - 1 - i
        if diff == 1:
            total_bribes += 1
            q[i], q[i + 1] = q[i + 1], q[i]
            i += 1
        elif diff == 2:
            total_bribes += 2
            q[i], q[i + 2] = q[i + 2], q[i]
            q[i], q[i + 1] = q[i + 1], q[i]
            i += 2
        elif diff > 2:
            print("Too chaotic")
            break
        i -= 1
    print(total_bribes)
    
def minimumBribes2(q): # Cannot work! have to rearrange from the back!
    # Write your code here
    tot = 0

    
    for i in range(len(q)):
        #print(i)
        diff = q[i] - i -1
        #print(i,val)
        if diff ==1:
            tot += 1
            q[i], q[i+1] = q[i+1], q[i]
            
        elif diff ==2:
            tot += 2
            q[i], q[i+2] = q[i+2], q[i]
            q[i], q[i+1] = q[i+1], q[i]
            
        elif diff >2:
            print("Too chaotic")

            return
        else:
            pass

    print(tot)
    
    
def minimumBribes3(q): # USE THIS FINAL
    # Write your code here
    tot = 0
    
    i = len(q)-1
    
    #for i in range(max_i,-1,-1):
    while i >= 0:
        #print(i)
        diff = q[i] - i -1
        #print(i,val)
        if diff ==1:
            tot += 1
            q[i], q[i+1] = q[i+1], q[i]
            i += 1
            
        elif diff ==2:
            tot += 2
            q[i], q[i+2] = q[i+2], q[i]
            q[i], q[i+1] = q[i+1], q[i]
            i += 2
            
        elif diff >2:
            print("Too chaotic")

            return
        else:
            pass
        i-=1
        
    print(tot)

if __name__ == '__main__':
    
    # q = [2, 1, 5, 3, 4]
    # q = [2, 5, 1, 3, 4]
    
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    

    minimumBribes3(q)