
#5 small,medium,large
def sml(num):
    if num<10:
        print("small")
    elif 10<num<100:
        print("medium")
    elif num>100:
        print("large")
    else:
        print("the given input is exactly 10 or 100")            

i=int(input("enter a number:"))
sml(i)        
