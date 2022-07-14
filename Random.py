import random
n=random.randint(1,10)
number=int(input("enter any number between 1 to 10(inclusive):"))
if(n==number):
    print("your guess is right")
else:
    print("your guess is wrong")
print("random number:",n)    
    
