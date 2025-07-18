a={1,2,3,4,4,5,5,7,7,8,9,12,45}
print(a)
print(type(a))
print(len(a))
for i in a:
    print(i)
print(2 in a)
print(22 not in a)
a.add(2453636)
print(a)
b={1,2,3,44,4,5,5,5,5,5}
print(b)
a.update(b)
print(a)
c={12,3,45,45,12,45,78,12}
d={12,23,34,45,46,5,67,8,78,12,3}
e=c.union(d)
print(e)
f=a.intersection(b)
print(f)
t=a.difference(b)
print(t)
z=c.symmetric_difference(d)
print(z)
c.remove(12)
print(c)
c.discard(2)
print(c)
d=a.pop()
print(d)
a.clear()
print(a)
# del d
# print(d)
a=["red","yellow","blue","violet","skyblue"]
a[2]="yullow"
print(a)
y=frozenset()
print(y)
y[1]="blue"
print(y)