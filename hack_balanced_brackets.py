# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 20:46:09 2021

@author: James Ang
"""

def isBalanced(s):
    # Write your code here
    
    
    while "{}" in s or "[]" in s or "()" in s:
        s = s.replace("{}","")
        s = s.replace("[]","")
        s = s.replace("()","")
        
    k = int(len(s)/2)
    
    for _ in range(k):
        if s[0] == '{' and s[-1] == "}":
            s = s[1:-1]
            
        elif s[0] == '[' and s[-1] == "]":
            s = s[1:-1]
            
        elif s[0] == '(' and s[-1] == ")":
            s = s[1:-1]
            
        else:
            return "NO"
    
    return "NO" if s else "YES"

if __name__ == "__main__":
    
    s = "{(([])[])[]]}"
    print(isBalanced(s))
    