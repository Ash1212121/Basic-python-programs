# a=open("file11.txt","x")
# b=open("file12.txt","x")
# c=open("file13.txt","x")
a=open("file11.txt","w")
a.write("hello good morning")
a.close()
a=open("file11.txt","r")
d=a.read()
c=open("file13.txt","w")
c.write(d)
b=open("file12.txt","w")
b.write("nice day")
b.close()
b=open("file12.txt","r")
f=b.read()
c=open("file13.txt","a")
c.write("\n"+f)


















