a={"name":"ash","age":"23","place":"triprayar","dist":"tsr","home":"chemmappilly"}
print(a)
print(len(a))
print(type(a))
print(a["home"])
print(a["dist"])
print(a["age"])
print(a["place"])
print(a["name"])
print(a.get("name"))
print(a.keys())
print(a.values())
print(a.items())
print("ash" in a)
print("name" not in a)
for i in a:
    print(i)
for i in a:
    print(a[i])
for i in a.keys():
    print(i)
for i in a.items():
    print(i)
for i in a.values():
    print(i)
a["dist"]="thrissur"
print(a)
a.update({"home":"veedu"})
print(a)
b=a.copy()
print(b)
c=dict(a)
print(c)
a.pop("name")
print(a)
a.popitem()
print(a)
del a
c.clear()
print(c)

#NESTED DICTIONARIES
a={"child1":{"name":"ashwin","age":12},
     "child2":{"name":"amal","age":23}}
print(a)
print(type(a))
print(len(a))
print(a["child1"])
print(a["child2"])
print(a["child1"]["age"])
print(a["child2"]["age"])
