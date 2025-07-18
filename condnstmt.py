x=30
y=50
if x>y:
    print(x,"is larger")
else:
    print(y,"is larger")

x=int(input("Enter a number"))
if x>10:
    print(x,"greater than 10")
else:
    print(x,"not greater than 10")

a=int(input("Enter a number"))
if a>0:
    print(a,"is a positive number")
elif a<0:
    print(a,"is a negative number")
else:
    print(a,"is zero")

a=int(input("Enter a number"))
if a%2==0:
    print(a,"is even number")
else:
    print(a,"is odd number")

a=int(input("Enter a number"))
if a%5==0:
    print(a,"is divisible")
else:
    print(a,"is not divisible")

a=int(input("Enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if a>b and a>c:
    print(a,"is the largest number")
elif b>a and b>c:
    print(b,"is the largest number")
else:
    print(c,"is larger")

a=int(input("Enter a number"))
if a%3==0 and a%5==0:
    print(a,"is divisible")
else:
    print(a,"is not divisble")

x=input("Enter the letter")
if x in "aeiouAEIOU":
    print(x,"is vowel")
else:
    print(x,"is consonent")

x=int(input("Enter the number"))
y=int(input("Enter the number"))
z=(input("Enter the operation(+,-,*,/)"))
if z=="+":
    print("result:",(x+y))
elif z=="-":
    print("result:",(x-y))
elif z=="*":
    print("result:",(x*y))
else:
    print("result:",(x/y))




















a=int(input("enter the number: "))
b=int(input("enter the number: "))
c=input("ENTER THE OPERATION(+,-,/,*)")
if c=="+":
    print("result:",(a+b))
elif c=="-":
    print("result:",(a-b))
elif c=="/":
    print("result:",(a/b))
else:
    print("result:",(a*b))
