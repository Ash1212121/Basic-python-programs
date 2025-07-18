# # find the even numbers from a range?
# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# for i in range(a,b+1):
#     if i%2==0:
#       print(i)

# # FIND THE SUM OF ODD NUMEBRS IN A RANGE?
# a=int(input("Enter the odd number: "))
# i=1
# sum=0
# for i in range(a+1):
#    if i%2!=0:
#       sum+=i
# print(sum)
    
# # FIND THE SUM OF EVEN NUMEBRS IN A RANGE?
# a=int(input("enter the even number: "))
# i=1
# sum=0
# for i in range(a+1):
#     if i%2==0:
#         sum+=i
# print(sum)

#  #FIND THE FACTORIAL OF A NUMBER?
# a=int(input("Enter the factorial of a number: "))
# i=1
# fact=1
# for i in range(2,a+1):
#    fact=fact*i
# print(fact)
  

#CHECK WHETHER A NUMBER IS PRIME OR NOT?
# a=int(input("enter a number: "))
# for i in range(2,a):
#    if a%i==0:
#     print("it is not prime number")
#     break
# else:
#    print("its prime number")

# #CHECK WHETHER A NUMBER IS PALINDROME OR NOT?
# a=input("Enter a palindrome number: ")
# b=""
# for i in range(len(a)-1,-1,-1):
#   b=b+a[i]
# if a==b:
#   print("its palindrome")
# else:
#   print("its not a palindrome")

# # #CHECK WHETHER A STRING IS PALINDROME OR NOT?
# a=input("Enter a palindrome text: ")
# b=""
# for i in range(len(a)-1,-1,-1):
#   b=b+a[i]
# if a==b:
#   print("its palindrome")
# else:
#   print("its not a palindrome")

# # #DISPLAY FIBONACCI SEQUENCE UPTO N TERMS?
# n = int(input("Enter number of terms: "))
# a, b = 0, 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# #CREATE A MULTIPLICATION TABLE FOR A NUMBER?
a=int(input("Enter a multiplication number: "))
for i in range(1,11):
    result =a*i
    print(a,"*",i,"=",result)

#CREATE A MULTIPLICATION TABLE FOR 10 NUMBERS?
for i in range(1, 11):  # Tables from 1 to 10
    for j in range(1, 11):  # Multiply each number from 1 to 10
        print(i * j, end=" ")
    print()  # Move to the next line after each table

# #COUNT THE NUMBER OF VOWELS IN A STRING? 
a=input("Enter a string: ")
vowel_count=0
for letter in a:
    if letter in "aeiouAEIOU":
        vowel_count+=1
if vowel_count==0:
   print("the no of string in a vowel is zero")
else:
    print("vowels in a string is",vowel_count)
        
    