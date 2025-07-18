#NUMBER
x=12
y=23.12
z=9+7j
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))

a=float(x)
print(a)
print(type(a))

b=complex(y)
print(b)
print(type(b))

d=complex(x)
print(d)
print(type(d))

#STRING
x="apple is a fruit with red colour"
print(x)
print(type(x))
print(len(x))
print(x[13:19])
print(x[12])
print(x[:15])
print(x[-10:-2])
print(x[-3])
print(x[:-6])
print("is" in x)
print("without" in x)
print("apple" not in x)
for i in x:
    print(i)