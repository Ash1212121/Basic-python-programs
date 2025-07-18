a={1,2,3,4,55,6,78,67,75}
print(a)
print(type(a))
print(len(a))
for i in a:
    print(i)
print(2 in a)
print(2 not in a)
a.add(123)
print(a)
b={12,23,34,45,56,67}
print(b)
a.update(b)
print(a)

c={123,124,125,126,127}
d={98,99,100,123,124,126}
z=c.union(d)
print
e=c.intersection(d)
print(e)
f=c.difference(d)
print(f)
g=c.symmetric_difference(d)
print(g)
c.remove(123)
print(c)
c.discard(1234)
print(c)
c.pop()
print(c)
c.clear()
print(c)