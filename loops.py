# break statement
i = 0

while i < 5:
    if i == 3:
        print("Executing 'break' statement in the next statment and the flow of execution is being", end = " ")
        break
    
    print(i)
    i += 1
    
print("shifted to here!")

# continue statement
i = 0
while i < 5:

    if i == 3:
        i += 1
        continue
    
    print(i)
    i += 1

# return statement
def sum():
    a = 10
    b = 20
    return a+b
ans = sum()
print(ans)
