l=list(map(int,input("enter the elements into list with duplication:").split(',')))
s=[]
for i in l:
    if i not in s:
        s.append(i)
print(s)        
