s1=input("enter a string:")
s2=input("enter another string:")
if(len(s1)==len(s2)):
    print("strings are with same length")
    result=''
    for i in range(len(s1)):
        result=result+(s2[i]+s1[i])
    print(result)
else:
    print("strings are with different lengths")
        
    
    
