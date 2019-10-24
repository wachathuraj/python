def add(a,b):
    print(a+b)

f=open("data.txt","r")
for i in f:
    x=i.split(" ")
    add(int(x[0]),int(x[1]))
f.close()
