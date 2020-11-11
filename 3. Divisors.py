from math import *

#Complexity: O(sqrt(n)) - efficient one
def divisors1(n):
    div = []
    for i in range(1, int(sqrt(n))+1):
        if(n%i == 0):
            div.append(i)
            if n//i != i:
                div.append(n//i)
    return div

#Complexity: O(n)
def divisors2(n):
    div = []
    for i in range(1, n+1):
        if (n % i == 0):
            div.append(i)
    return div

t = int(input())
while t:
    n = int(input())
    result1 = divisors1(n)
    result1.sort()
    print(*result1)

    result2 = divisors2(n)
    print(*result2)

    t = t-1