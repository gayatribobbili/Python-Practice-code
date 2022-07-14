from decimal import*
num1=Decimal(input("enter a number to 1:"))
num2=Decimal(input("enter a number to 2:"))
diff=abs(num1-num2)
if(diff<=0.001):
    print("close")
else:
    print("not close")
    
