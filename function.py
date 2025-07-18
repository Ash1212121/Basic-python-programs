def name():
    print("how are you")
name()
name()

a=int(input("Enter the first number: "))
b=int(input("Enter the second number"))
def add():
    print(a+b)
add()

def sub():    #global variable:fun porath kodknth aan global varble,pinne aaa fun throughout access indavilaaa.
    print(a-b)
sub()

def multi():   #local variable:function ullil kodknth aaan local variable.
    a=1
    b=8
    print(a*b)
multi() 

def add(a,b):
    print(a+b)
add(2,3)

def multi(a,b):
    print(a*b)
variable=int(input("Enter a number: "))
variable1=int(input("Enter a number: "))
multi(variable,variable1)

# CHECK WHETHER A NUMBER IS EVEN OR NOT USING FUNCTION?
a=int(input("Enter a number: "))
def even(x):
    if x%2==0:
        print("it is an even number: ")
    else:
        print("it is odd")
even(a)

#FIND THE SUM OF FIRST N NATURAL NUMBERS USING FUNCTION?
a=int(input("Enter a number: "))
def add(x):
    sum=0
    for i in range(x+1):
        sum+=i
    print(sum)
add(a)
    
# FIND THE SUM OF EVEN NUMBERS IN A RANGE using function?
a=int(input("Enter a number: "))
def even(x):
     sum=0
     for i in range(x+1):
        if i%2==0:
         sum+=i
     print(sum)
even(a)
    
# FIND THE SUM OF ODD NUMEBRS IN A RANGE?
a=int(input("Enter a number: "))
def odd(x):
    sum=0
    for i in range(x+1):
        if i%2!=0:
            sum+=i
    print(sum)
odd(a)

# FIND THE FACTORIAL OF A NUMBER?
a=int(input("Enter a number: "))
def fat(x):
    fact=1
    for i in range(1,x+1):
         fact*=i
    print(fact)
fat(a)

#CHECK WHETHER A NUMBER IS PRIME OR NOT? 
a=int(input("Enter a number: "))
def num(x):
    prime=1
    for i in range(2,a):
        if a%i==0:
            print("it is not a prime number")
            break
    else:
        print("It is a prime number")
num(a)

# def name(x,y):
#     print(x+y)
# name(1,2)

# def arbitrary(*x):
#     print(x[6])
# arbitrary(1,2,3,4,5,6,7,8,678)

# def key(c,d,e):
#     print(c+d)
# key(c=342,d=450,e=890)

# def arbkeyarg(**a):
#     print(a["b"])
# arbkeyarg(a=12,b=23,c=34,d=56,e=123)

# def defaultparameter(x=9):
#     print(x)
# defaultparameter()

def returnstmt(x):
    return(x+10)
print(returnstmt(23))

#write a function to find the sum of list of numbers?
a=[10,5,12,3,5]
def add(x):
    sum=0
    for i in a:
        sum+=i
    print(sum)
add(a)

#find the area of a circle using function?
# a=int(input("Enter a number: "))
def area(r):
    circle=1
    pi=3.14
    circle=pi*r*r
    print("Area of circle is:",circle)
a=int(input("Enter the number: "))
area(a)