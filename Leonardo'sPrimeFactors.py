#!/bin/python3
#problem desc @ https://www.hackerrank.com/challenges/leonardo-and-prime/problem

import os
import sys

#
# Complete the primeCount function below.
#

primes_found = {} #instead of recomputing primes, we keep a dictionary of primes discovered, to prevent wasted computation

def prime(n):
    try:
        return primes_found[n]
    except KeyError:
        for i in range(2,n//2): #we only need to check up to half of N because nothing can divide into N once its above half of N
            if n%i == 0:
                return False
        primes_found[n] = True
        return True

def primeCount(n):
    #
    # Write your code here.
    #
    _sum = 2
    primes=1
    if n <=1:
        return 0
    elif n <=3:
        return primes
    else:
        for i in range(3,n,2): #only checking odd numbers, as primes after 2 are odd
            if prime(i):
                outcome = _sum*i
                if outcome>n:
                    return primes
                _sum*=i
                primes+=1
    
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
