"""print("Hello World!")
print("ashwin kd")
name="john"
age=25
height=5.8
is_student=True
print("Name:",name)
print("Age:",age)
print("Height:",height)
print("is_student:",True)"""
"""x=12
y=45.3
z=3+4j
#x=12,converting int to float
a=float(x)
print(a)
print(type(a))
#z=complex to integer
c=int(y)
print(c)
print(type(c))"""
"""a="sreee rama kshethram is situated in triprayar east nada"
print(a)
print(type(a))
print(len(a))
print(a[1])
print(a[2:17])
print(a[-2:])
print(a[:6])
print(len(a))
print(a[:55])
print(a[17:])
print(a[-17:-9])
print("is" in a)
print("is" not in a)
for i in a:
    print(i)"""
"""a="amla is a tropical ayurvedic used substsance"
print(a.upper())
print(a.lower())
print(a.split("a"))
b="   trip yarrr   "
print(b)
print(b.strip())
print(b.replace("trip","trap"))
print(a.count("c"))"""    
a=["maddy","francy","joshy","kd","thankan"]
print(a)
print(len(a))
print(type(a))
print(a[4])
print(a[2:4])
print(a[-3:-1])
print(a[:-3])
print("is" in a)
print("is" not in a)
a[1]="raju"
print(a)
a.append("maga")
print(a)
a.insert(3,"thenka")
print(a)

b=["magazine","manager","photo"]# used to add elements from an iterable (like a list, tuple, set, or string) to the end of an existing list.
b.extend(a)
print(b)

a.sort()#sorting in alphabetic order[ascending-descending]
print(a)

a.sort(reverse=True)#descending-ascending order
print(a)

a.copy()
print(a)

c=list(a)
print(c)
print(b+c)

print(a.count("kd"))#to count how much name or objects are there

a.remove("maga")#to remove the specified ones
print(a)

a.pop(2)#we can delete the specified ones
print(a)

del a[2]#doubt
print(a)

a.clear(a)
print(a)
