#Complexity of this program is O(1) as we used the famous Gaussian formula, otherwise it would've been O(n),
#if we followed looping convention/ iteration

def summation(n):
    return (n*(n+1))//2     #// will give us int value, cutting of the fractinal parts

t = int(input())            #this is our test case
while t:
    n = int(input())
    print("The resultant sum is {}".format(summation(n)))
    t = t-1
