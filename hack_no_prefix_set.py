# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 15:07:25 2021

@author: James Ang
"""

def noPrefix(words):
    # Write your code here
    for i in range(len(words)):
        w = words.pop(0)
        ind = [w in i for i in words]
        
        if True in ind:
            loc = ind.index(True)
            print("BAD SET")
            print(words[loc])
            break
        else:
            print("GOOD SET")

def noPrefix1(words):
    # Write your code here
    for i, val in enumerate(words):
        #print(f"\ni:{i}")
        #print(val)
        
        if i>0:
            for j in range(i):
                #print(f"j:{j}")
                if words[j] in val:
                    print("BAD SET")
                    print(val)
                    return
                
    print("GOOD SET")

def noPrefix2(words): # solution
    ht_prefix = {}
    ht_word = {}
    for w in words:
        check = ''
        if w in ht_prefix:
            print("BAD SET")
            print(w)
            return
        for l in w:
            check += l
            ht_prefix[check] = 1
            if check in ht_word:
                print("BAD SET")
                print(w)
                return
        ht_word[w] = 1
    print("GOOD SET")

if __name__ == '__main__':

    #words = ['aab', 'defgab', 'abcde', 'aabcde', 'cedaaa', 'bbbbbbbbbb', 'jabjjjad']
    words = ['aab', 'aac', 'aacghgh', 'aabghgh']


    noPrefix2(words)