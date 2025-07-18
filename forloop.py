a=("str")
print(a)
print(type(a))
for i in a:
    print(i)

# a=[1,2,3,4,5,6,7,8]
# print(a)
# print(type(a))
# for i in a:
#     print(i)

# a=(23,34,45,56,67,78,89)
# print(a)
# print(type(a))
# for i in a:
#     print(i)

# a={12,23,34,54,45,5,656,89}
# print(a)
# print(type(a))
# for i in a:
#     print(i)

# a={"class":"five","name":"ash","age":23}
# print(a)
# print(type(a))
# for i in a:
#     print(i)

# for i in range(11):
#     print(i)
# for i in range(1,11):
#     print(i)
# for i in range(1,11,2):
#     print(i)
# for i in range(2,11,2):
#     print(i)

for i in range(10,0,-1):
    print(i)
for i in range(1,11):
    print(i)
    if i==5:
        break
for i in range(1,11):
    if i==5:
        continue
    print(i)

#FIND THE EVEN NUMBERS FROM A RANGE
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
for i in range(a,b+1):
    if i%2==0:
        print(i)

# #FIND THE SUM OF ODD NUMEBRS IN A RANGE?
# #FIND THE FACTORIAL OF A NUMBER?
# #CHECK WHETHER A NUMBER IS PRIME OR NOT?
# #CHECK WHETHER A NUMBER IS PALINDROME OR NOT?
# #CHECK WHETHER A STRING IS PALINDROME OR NOT?
# #DISPLAY FIBONACCI SEQUENCE UPTO N TERMS?
# #CREATE A MULTIPLICATION TABLE FOR A NUMBER?
# #COUNT THE NUMBER OF VOWELS IN A STRING? 

#FIND THE SUM OF FIRST N NATURAL NUMBERS?
a=int(input("enter the natural no: "))
i=1
sum=0
for i in range(a+1):
    sum=i+sum
print(sum)

#FIND THE FACTORIAL OF A NUMBER?
a=int(input("Enter the factorial of: "))
fact=1
for i in range(1,a+1):
  fact*=i
print(fact)
 
# FIND THE SUM OF ODD NUMEBRS IN A RANGE?
a=int(input("Sum of Odd numbers: "))
i=1
sum=0
for i in range(a+1):
  if i%2!=0:
    sum=i+sum
print(sum)

#CHECK WHETHER A NUMBER IS PRIME OR NOT? 
a=int(input("Enter a prime number: "))
for i in range(2,a):
   if a%i==0:
      print("it is not a prime number")
      break
else:
   print("it is a prime number")

# CHECK WHETHER A NUMBER IS PALINDROME OR NOT?
a=int(input("Enter a palindrome number: "))
or_number=a
rev_number=0
while a>0:
    b=a%10
    rev_number=rev_number*10+b
    a=a//10 
if or_number==rev_number:
    print("it is palindrome number")
else:
     print("it is not a palindrome")

# CREATE A MULTIPLICATION TABLE FOR A NUMBER?
a=int(input("MULTIPLICATION TABLE FOR A NUMBER"))
for i in range(1, 11):
     result = a * i
     print(a,"*", i, "=", result)

# COUNT THE NUMBER OF VOWELS IN A STRING? 
a=input("Enter  a string:")
vowel_count=0
for letter in a:
     if letter in "aeiouAEIOU":
          vowel_count=vowel_count+1
if vowel_count==0:
 print("the number of vowels in a string is zero")
else:
    print("no of vowels in a string is",vowel_count)
     
