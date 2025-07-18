a=(1,2,2,3,3,4,4,4,5,5,5,)
print(a)
print(type(a))
print(len(a))
print(a[1:2])
print(a[:2])
print(a[1])
print(a[-4:-1])
print(a[-4])
print(a[:-3])
print(1 in a)
print(2 not in a)
for i in a:
    print(i)
print(a[2])
b=(234,)
c=list(a)
print(c)
c.append(2)
print(c)
c.insert(1,22)
print(c)
print(a+b)
print(a.count(3))
print(a*4)
a=tuple(c)
print(a)







