def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

ans = fact(5)
print(ans)
        
