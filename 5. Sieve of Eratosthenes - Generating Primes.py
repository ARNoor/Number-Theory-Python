#Complexity of Sieve of Eratosthenes is O(N log(log N))
from math import *
t = int(input())

def generatingPrimes(n):
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    for i in range(2, int(sqrt(n))+1):
        if(primes[i]):
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes

def printPrimes(res):
    for i in range(0, len(res)):
        if(res[i]==True):
            print(i, end=" ")

while t:
    n = int(input())
    res = generatingPrimes(n)
    printPrimes(res)
    t = t - 1