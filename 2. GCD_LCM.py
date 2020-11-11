#Stein's is computationally effective, as multiplying by 2 or divison by 2 is much favorable by our computers
#than doing modular operation
import time

def GCD_Euclid(u, v):
    if u == 0:
        return v
    elif v == 0:
        return u
    else:
        return GCD_Euclid(v % u, u)

def GCD_Steins(u, v):
    if u == 0:
        return v
    elif v == 0:
        return u
    elif u % 2 == 0 and v % 2 == 0:
        return 2*GCD_Steins(u/2, v/2)
    elif u % 2 == 0 and v % 2 != 0:
        return GCD_Steins(u/2, v)
    elif u % 2 != 0 and v % 2 == 0:
        return GCD_Steins(u, v/2)
    else:
        if u > v:
            return GCD_Steins((u-v)/2, v)
        else:
            return GCD_Steins((v-u)/2, u)

def lcm(u, v):
    return (u*v)//GCD_Steins(u, v)

t = int(input())
while t:
    a = int(input())
    b = int(input())
    start = time.time()
    gcd_S = GCD_Steins(a, b)
    end = time.time()
    print("{} - Time taken for Stein's {}".format((gcd_S),(end - start)))

    start = time.time()
    gcd_E = GCD_Euclid(a, b)
    end = time.time()
    print("{} - Time taken for Euclid's {}".format((gcd_E),(end - start)))

    print("And the LCM is {}".format(lcm(a, b)))
    t = t - 1




