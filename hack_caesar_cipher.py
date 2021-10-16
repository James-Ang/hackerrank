# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 11:54:33 2021

10
www.abc.xy
87

fff.jkl.gh

@author: James Ang
"""


def caesarCipher(s, k):
    ori = "abcdefghijklmnopqrstuvwxyz"
    if k > 24:
        k = k%26
    print(f"k : {k}")
    lower = ori[k:] + ori[:k]
    
    list_s= list(s)
    list_ori = list(ori)
    list_lower = list(lower)
    
    for j, value in enumerate(list_s):
        if value in list_lower:
            ind = list_ori.index(value)
            list_s[j] = list_lower[ind]
        
        elif value.isupper():
            value_lower = value.lower()
            ind = list_ori.index(value_lower)
            list_s[j] = list_lower[ind].upper()
            
        else:
            pass
 
    final = "".join(list_s)
            
    return final

# s= "middle-Outz"
s = "www.abc.xy"
k = 87
result = caesarCipher(s, k)
