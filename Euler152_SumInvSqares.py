#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 22:41:21 2017

@author: christophergreen

Writing 1/2 as a sum of inverse squares
Problem 152
There are several ways to write the number 1/2 as a sum of inverse squares using distinct integers.

For instance, the numbers {2,3,4,5,7,12,15,20,28,35} can be used:



In fact, only using integers between 2 and 45 inclusive, there are exactly three ways to do it, 
the remaining two being: {2,3,4,6,7,9,10,20,28,35,36,45} and {2,3,4,6,7,9,12,15,28,30,35,36,45}.

How many ways are there to write the number 1/2 as a sum of inverse squares using distinct integers
 between 2 and 80 inclusive?
"""

import itertools

def inv_squares():
    inv=[]
    for i in range(2,81):
        inv.append(i**-1)
    #print(inv_squares)
    return inv 
    
def assemble_iters(num):
    count=0
    for i in itertools.combinations(inv_squares(),num):
        if sum(i)==.5:
            count+=1
    print("found",count,"equivalents to 1/2 using any",num,"pairs from inv_squares")
    return count

def main(maximum):
    out=0
    k=2
    while k<=maximum:
        out+=assemble_iters(k)
        k+=1
    print("")
    print("from 2 through",maximum,"there are",out,"equivalents to 1/2 from the inv_squares")
    return out

"""
main(10)
found 1 equivalents to 1/2 using any 2 pairs from inv_squares
found 5 equivalents to 1/2 using any 3 pairs from inv_squares
found 22 equivalents to 1/2 using any 4 pairs from inv_squares
found 83 equivalents to 1/2 using any 5 pairs from inv_squares
found 317 equivalents to 1/2 using any 6 pairs from inv_squares
"""
def check(minim):
    i=80
    sum=0
    while i>=minim:
        sum+=(i**-1)
        i-=1
    print("sum from 80 down thruogh",minim,"is",sum)
    return



"""
    iters=list(itertools.combinations(inv_squares,num))
    count=0
    print("the number of iterations choosing",num,"items is",len(iters))
    for ite in iters:
        if sum(ite)==.5:
            #print(sum(ite))
            count+=1
    print("")
    print("found",count,"equivalents to 1/2 using any",num,"pairs from inv_squares")
    return count
"""