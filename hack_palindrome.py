# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 11:54:33 2021

10
www.abc.xy
87

fff.jkl.gh

@author: James Ang
"""

import copy


def palindromeIndex(s):
    # Write your code here
    s_list = list(s)
    
    def remove_char(s,i):
        
        first = s[:i]                                        
        last = s[i+1:]
        
        return first + last
    s_new = copy.deepcopy(s_list)
    if s_new == s_new[::-1]:
        ind =-1
    else:
        for i, val in enumerate(s_list):
            print(i,val)
            s_temp = copy.deepcopy(s_list)
            
            s_new = remove_char(s_temp,i)
            #s_new.remove(val)
            
            if s_new == s_new[::-1]:
                ind = i
                break
            else:
                ind =-1
    
    return ind

def palindromeIndex2(s): # failed
    
    n = int((len(s) - 1)/2)
    
    first_half = s[:n]
    last_half = s[n:][::-1]
    
    def remove_char(s,i):
        
        first = s[:i]                                        
        last = s[i+1:]
        
        return first + last
    
    
    
    for i in range(n):
        print(i)
        if first_half[i] ==last_half[i]:
            
            print("yay")
            print(first_half[i],last_half[i])
            
        else:
            
            print("nay")
            print(first_half[i],last_half[i])
            
            # test remove right
            last_half1 = remove_char(last_half,i)
            
            if last_half1 == first_half:
                print("yay")
                ind = len(s) - i
                # print(len(s))
                last_half = last_half1
            
            else:
                first_half1 = remove_char(first_half,i)
                if first_half1 == last_half:
                    print("yay")
                    ind = i
                    print(i)
                    last_half = last_half1
                
            
    print(first_half, last_half)
    print(ind)
    
    # for i in range(len(s)):
    #     if s[i] ==s[i-1]:
    #         print("yay")
            
    #     else:
    #         print("nay")
    

def palindromeIndex3(s):
    
    # 1) Determine mismatching pair
    
    def find_mismatch(s):
        
    
        i = 0
        j = len(s) -  1
        
        while i<j and s[i] == s[j]:

            i+=1
            j-=1

        return i, j

    def is_palindrome(s):
        i, j = find_mismatch(s)
        
        return j <= i
        

    
    def correct(s):
        i, j = find_mismatch(s)
        
        # if is_palindrome(s):
        #     ind = -1
        
        if is_palindrome(s):
            ind = -1
        else:
            if is_palindrome(s[i+1 : j+1]):
                ind = i
            else:
                ind = j
            
        return ind
        #return -1 if j <= i else i if is_palindrome(s[i+1 : j+1]) else j 

    
    #print("Palindrome: ",is_palindrome(s))
    print(correct(s))

if __name__ == '__main__':

    s = "bacbaabcab"
    
    res = palindromeIndex3(s) # use palindrome3