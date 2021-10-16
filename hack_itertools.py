# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:11:59 2021

itertools = iteration tools

@author: James Ang
"""

from itertools import product, combinations, permutations, combinations_with_replacement

#type help(product)
# class product(builtins.object)
#  |  product(*iterables, repeat=1) --> product object
#  |  
#  |  Cartesian product of input iterables.  Equivalent to nested for-loops.
#  |  
#  |  For example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).
#  |  The leftmost iterators are in the outermost for-loop, so the output tuples
#  |  cycle in a manner similar to an odometer (with the rightmost element changing
#  |  on every iteration).
#  |  
#  |  To compute the product of an iterable with itself, specify the number
#  |  of repetitions with the optional repeat keyword argument. For example,
#  |  product(A, repeat=4) means the same as product(A, A, A, A).
#  |  
#  |  product('ab', range(3)) --> ('a',0) ('a',1) ('a',2) ('b',0) ('b',1) ('b',2)
#  |  product((0,1), (0,1), (0,1)) --> (0,0,0) (0,0,1) (0,1,0) (0,1,1) (1,0,0) ...

list(product([1,2],repeat=2))

A = [1,2]
B = [2,3]
print(*product(A,B))


# Permutations
word,k = "HACK", "2"
print(word,k)
a = list(permutations(word,int(k)))
print(list(permutations(word,int(k))))

l= sorted(["".join(i) for i in a])
for i in l:
    print(i)


# Combinations
print(list(combinations(word,int(k))))
word = sorted(word)

for j in range(int(k)):
    for i in list(combinations(word,j+1)):
        print("".join(i))
        
# COMBINATIONS WITH REPLACEMENTS

print(list(combinations_with_replacement(word,int(k))))
word = sorted(word)
for i in list(combinations_with_replacement(word,int(k))):
    print("".join(i))