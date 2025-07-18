import module
print(module.add(2,3))
print(module.div(120,23))
print(module.multi(234,21))
print(module.sub(12313341,4524))
import math
print(max(23,435,654647,4346,457567,3456)) 
print(min(12323424,2342,3423423,234242))
print(abs(-23)) #converting -ve to +ve
print(pow(2,3)) #to find power
print(math.pi)
print(math.factorial(3))
print(math.log10(1000))
print(math.floor(9.22))
print(math.ceil(2.333))

#find the area of a circle using math module?
#area of a cylinder suing math function?
#volume of sphere?
#volume of cylinder?

#find the area of a circle using math module?
# import math
# a=int(input("Enter the number: "))
# r=a*a
# circle=math.pi*r
# print(circle)

# #area of a cylinder using math function?
# r=int(input("Enter a number: "))
# h=int(input("Enter a number: "))
# area=2*r*r+2*r*h
# cylinder=math.pi*area
# print(cylinder)

# #volume of sphere?
# r=int(input("Enter the number: "))
# h=int(input("Enter a number: "))
# volume=r*r*h
# sphere=math.pi*volume
# print(cylinder)

# #volume of cylinder?
# r=int(input("Enter the number: "))
# h=int(input("Enter a number: "))
# volume=4/3*r*r*h
# cylinder=math.pi*volume
# print(cylinder)

import datetime
# a=datetime.datetime.now()
# print(a)
# print(a.strftime("%A"))
# print(a.strftime("%a"))
# print(a.strftime("%B"))
# print(a.strftime("%b"))
# print(a.strftime("%d"))
# print(a.strftime("%m"))
# print(a.strftime("%Y"))
# print(a.strftime("%y"))
# print(a.strftime("%H"))
# print(a.strftime("%I")) #24hr time [if 1pm--13:11pm]
# print(a.strftime("%M")) #minute
# print(a.strftime("%S")) #second
# print(a.strftime("%f")) #microseconds
# print(a.strftime("%p")) #AM or PM
# print(a.strftime("%C")) #century
# print(a.strftime("%j")) #eee kollathile innathe divsm kandpidikn

# a=datetime.datetime(2003,6,24)
# print(a.strftime("%A"))

# a=lambda b,c:b+c
# print(a(234442,324234242423))

# b=lambda c,d,e:c*d*e
# print(b(2,3,2))

# a=["apple","grape","greenapple","jackfruit","mango"]
# b=list(map(lambda fruit:fruit.upper(),a))
# print(b)

# a=["RED","BLUE","YELLOW","VIOLET","GREY"]
# b=list(map(lambda color:color.lower(),a))
# print(b)

# a=[2,5,3,6,10,5]
# b=list(filter(lambda number:number>5,a))
# print(b)

#find the even numbers from a list using lambda function?
# a=[24,23,21,26,56,88,20,28,34]
# b=list(filter(lambda i:i%2==0,a))
# print(b)

#square the list of numbers using lambda function?
# a=[2,3,4,5,5,6,6,7,7,9,8.12,23]
# b=list(map(lambda c:c*c,a))
# print(b)

#square only even numbers in a list?
# a=[22,223,34,56,67,98,88,66,60]
# b=list(filter(lambda i:i%2==0,a))
# print(b)
# c=list(map(lambda i:i*i,b))
# print(c)

#double the odd numbers only?
# a=[56576,7656535,2232,1,3,5,7,9,9]
# b=list(filter(lambda i:i%2!=0,a))
# print(b)
# c=list(map(lambda i:i+i,b))
# print(c)

#calculate the length of a string in a list?
a=["yellow","red","blue","green","violet","skyblue"]
b=list(map(lambda str:len(str),a))
print(b)
#find the negative numbers from a list?
a=[12,24,56,34,-34,-67,-45,-12]
b=list(filter(lambda negative:negative<0,a))
print(b)