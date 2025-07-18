try:
    print(x)
except:
    print("there is eror")
else:
    print("no error")
finally:
    print("prgm complted successfully")
try:
    print(x)
except NameError:
    print("Check the variable")
except:
    print("ERROR FOUND")
a=int(input("enter a postive number"))
if a<0:
    raise Exception("negative numbers are not allowed")
else:
    print("CORRECT")
 