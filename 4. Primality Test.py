from math import *
def trial_division_test(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if(n % i == 0):
            return False
    return True

def trial_division_modified(n):
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(sqrt(n))+1, 4):
        if (n % i == 0) or (n % (i+2) == 0):
            return False
    return True

t = int(input())
while t:
    n = int(input())
    res1 = trial_division_test(n)
    res2 = trial_division_modified(n)
    print("{} is prime - {}".format(n, res1))
    print("{} is prime - {}".format(n, res2))
    t = t - 1