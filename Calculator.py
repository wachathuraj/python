for i in range(1,10):
    x=str(input("Input Two Numbers with Arithmatic:::"))
    if(("+" in x)==True):
        y=x.split("+")
        z=int(y[0])+int(y[1])
        print(z)
    elif(("-" in x)==True):
        y=x.split("-")
        z=int(y[0])-int(y[1])
        print(z)
    elif(("*" in x)==True):
        y=x.split("*")
        z=int(y[0])*int(y[1])
        print(z)
    elif(("/" in x)==True):
        y=x.split("/")
        z=int(y[0])/int(y[1])
        print(z)
input("press <Enter> to exit")   
