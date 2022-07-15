import random
l=[]
for i in range(20):
    l.append(random.randint(1,100))
print("list:",l)
print("average:",round(sum(l)/len(l),2))
print("largest value in the list:",max(l))
print("smallest value in the list:",min(l))
l1=sorted(l)
print("second largest value in the list:",l1[-2])
print("second smallest value in the list:",l1[1])
count=0
for i in l:
    if i%2==0:
        count+=1
print("number of even numbers in the list:",count)
    

