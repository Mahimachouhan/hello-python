n = int(input())


def factorial(n):
    fact=1
    if n==0 | n==1:
        return 1
    for i in range (1,n+1):
        fact*=i
    return fact

print(factorial(n))