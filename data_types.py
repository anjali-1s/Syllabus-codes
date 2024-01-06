x = 10
print(x, "is a type of", type(x))

str = "Anjali"
print(str,"is a type of",type(str))

z = 1+2j
print(z,"is a type of",type(z))
print(z,"is a complex number?",isinstance(z,complex))

print("is",str,"is an integer type variable?",isinstance(str,int))

age = 20
print(id(age))

age = 30
print(id(age))

#Global variable
x = "Global variable"
def foo():
    # x = x - 1   provides an error bcz it is treated as local variable and yet none of the local variable is defined here.
    print(x)
foo()
print(x)

#Local Variable
def fun():
    y = 10
    print(y)
fun()
# print(y) it will provide an error bcz it is a local variable.


# Implicit conversion
a = 10.0
b = 20.0
mul = a * b
print(mul)
print(type(mul))

# Explicit conversion
n = 10.8
num = int(n)
print(type(n))
print(type(num))

#end parameter in print()
print("Welcome",end = " ")
print("to coding ninjas!",end = "@")

#sep parameter in print()
print("coding",sep = '')
print("ninjas",sep = " @ ")
print("hello","world",sep = " ")

#input through split()
x,y = input().split()
print(x,y)


