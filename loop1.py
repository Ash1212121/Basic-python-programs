# #PRINTING 1-10 NUMBERS USING WHILE LOOP
# i=1
# while i<=10:
#     print(i)
#     i+=1

# #PRINTING 20-35 NUMBERS USING WHILE LOOP
# i=20
# while i<=35:
#     print(i)
#     i+=1
# #printing even numbers from 1-10
# i=1
# while i<=10:
#     if i%2==0:
#         print(i)
#     i+=1
# #div by 3 and 5
# i=1
# while i<=20:
#     if i%3==0 or i%5==0:
#         print(i)
#     i+=1
# ##PRINT NUMBERS FROM 1-10 AND BREAK IT IN 5TH POSN USING WHILE LOOP
i=1
while i<=10:
    print(i)
    if i==5:
        break
    i+=1
# #PRINT NUMBERS FROM 1-10 AND CONTINUE IT IN THE 5TH POSN USING WHILE LOOP
# i=1
# while i<=10:
#     i+=1
#     if i==5:
#         continue
#     print(i)

# SUM OF 10 NUMBERS USING WHILE LOOP
i=1
sum=0
while i<=10:
    sum+=i
    i+=1
print(sum)

#FIND THE SUM OF EVEN NUMBERS FROM 1-10
i=0
sum=0
while i<=10:
    if i%2==0:
        sum+=i
        i+=2
print(sum)

#find the sum of odd numbers from 1-10
i=1
sum=0
while i<=10:
    if i%2!=0:
        sum+=i
        i+=2
print(sum)

#find the factorial of the number?
a=int(input("Enter the number: "))
i=1
fact=1
while i<=a:
    fact=fact*i
    i+=1
print(fact)

a=("str")
print(a)
print(type(a))
for i in a:
    print(i)