# #PRINTING 1-10 NUMBERS USING WHILE LOOP
i=1
while i<=10:
    print(i)
    i+=1

# #PRINTING 20-35 NUMBERS USING WHILE LOOP
i=20
while i<=35:
    print(i)
    i+=1

# #PRINT EVEN NUMBERS FROM 1-10 USING WHILE LOOP
i=2
while i<=10:
    print(i)
    i+=2

# #PRINTING ODD NUMEBRS FROM 1-10 USING WHILE LOOP
i=1
while i<=10:
    if i%2!=0:
        print(i)
    i+=1
# #FIND NUMBERS FROM 1-20 WHICH IS DIV BY BOTH 3 AND 5 USING WHILE LOOP
i=1
while i<=20:
    if i%3==0 or i%5==0:
      print(i)
    i+=1        
# #PRINT NUMBERS FROM 1-10 AND BREAK IT IN 5TH POSN USING WHILE LOOP  
i=1
while i<=10:
    print(i)
    if i==5:
        break
    i+=1

# #PRINT NUMBERS FROM 1-10 AND CONTINUE IT IN THE 5TH POSN USING WHILE LOOP
i=0
while i<10:
    i+=1
    if i==5:
     continue
    print(i) 

# SUM OF 10 NUMBERS USING WHILE LOOP
i=1
sum=0
while i<=10:
    sum+=i
    i+=1
print("RESULT: ",sum)

# # FIND THE SUM OF EVEN NUMBERS FROM 1-10
x=int(input("enter a limit"))                 
i=1
sum=0
while i<=x:
    if i%2==0:
        sum+=i #sum=sum+i
        i+=1
print(sum)

# #find the factorial of the number
# x=int(input("Enter the number:"))
# i=1
# a=1
# while i<=x:
#     a*=i
#     i+=1
# print(a)