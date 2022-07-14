import random
l=[]
for i in range(100):
    l.append(random.randint(0,1))
maxzero=0
count=0
for i in range(len(l)):
    if(l[i]==0):
        count+=1
    if(i==len(l)-1):
        if count>maxzero:
            maxzero=count
    if(l[i]==1):
        if count>maxzero:
            maxzero=count
        count=0
print("longest run of zeros in a row is",maxzero)        
print("the list ",l)
