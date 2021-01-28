# First Problem:
'''
A positive integer m can be partitioned as primes if it can be written as p + q where p > 0, q > 0 and both p and q are prime numbers.

Write a Python function primepartition(m) that takes an integer m as input and returns True if m can be partitioned as primes and False otherwise. 
(If m is not positive, your function should return False.)

'''

# SOLUTION - 

def isPrime(n):
  import math 
  if n < 2:
    return False
  for i in range(2, int(math.sqrt(n))+1, 1):
    if n%i == 0:
      return False
  return True

def primepartition(m):
  if m < 2:
    return False
  for i in range(2, m//2+1, 1):
    if isPrime(i) and isPrime(m-i):
      return True
  return False
