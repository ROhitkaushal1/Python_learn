num = int(input("write down the number"))
if(num%4==0):
    if(num%400==0):
        if(num%100!=0):
            print("it is a leap year")
else:
    print("this is not a leap year")