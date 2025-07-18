list_of_froots=["apple","grapes","melon","pineaplle","jackfruit"]
print(list_of_froots)
print(type(list_of_froots))
print(len(list_of_froots))
print(list_of_froots[2])
print(list_of_froots[1:3])
print(list_of_froots[:4])
print(list_of_froots[2:])
print(list_of_froots[-1:])
print(list_of_froots[-4:-1])
print(list_of_froots[:-2])
print("apple" in list_of_froots)
print("grapes" not in list_of_froots)
for i in list_of_froots:
    print(i)
   
list_of_froots[1]="mundiri"
print(list_of_froots)

list_of_froots.append("mango")
print(list_of_froots)

list_of_froots.insert(2,"papaya")
print(list_of_froots)

list1=["mobile","harddrive","CD"]
list_of_froots.extend(list1)
print(list_of_froots)

list_of_froots.sort()
print(list_of_froots)
list_of_froots.sort(reverse=True)
print(list_of_froots)

# z=list1.copy()
# print(z)

# h=list(list_of_froots)
# print(h)
# print(z+h)

# print(list_of_froots.count("mundiri"))
# list_of_froots.remove("CD")
# print(list_of_froots)
# list_of_froots.pop(4)
# print(list_of_froots)
# list_of_froots.pop()
# print(list_of_froots)
# del list_of_froots[3]
# print(list_of_froots)
# list_of_froots.clear()
# print(list_of_froots)
# del list_of_froots
# print(list_of_froots)
