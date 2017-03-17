mark=float(input("insert your mark:"))
if 0<=mark<=100:
    if mark>=75 :
        print("A")
    elif mark>=65 :
        print("B")
    elif mark>=55 :
        print("C")
    elif mark>=35 :
        print("S")
    else :
        print("W")
else:
    print("invalide mark.plese check your mark.")
input("press <Enter> to exit")        
