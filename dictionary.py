a={"name":"ashwin","age":"12","place":"thrissur","number":12345}
print(a)
print(type(a))
print(len(a))
print(a["name"])
print(a["number"])
print(a["age"])
print(a["place"])
print(a.get("name"))
print(a.keys())
print(a.values())
print(a.items())
print("name" in a)
print("ashw" not in a)
for i in a:
    print(i)
for i in a:
    print(a[i])
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)
a["age"]=12
print(a)
a.update({"place":"mannavanur"})
print(a)
a["home"]="nalloruveedu"
print(a)
a.update({"home":"nalloru"})
print(a)
b=a.copy()
print(b)
d=dict(a)
print(d)
a.pop("name")
print(a)
a.popitem()
print(a)
del a["age"]
print(a)
a.clear()
print(a)
del a

family={"child1":{"name":"machan","age":65},"child2":{"name":"max","age":56},"child3":{"name":"ammalu","age":45}}
print(family)
print(family["child2"])
print(family["child2"]["age"]) 

