#Create a list of 10 random numbers between 10 and 50 
#Then sum those 
#then print that list and its sum 
import random

lst = []
for e in range(0,10,1):
    e = random.randint(10,50)
    lst.append(e)
    
a,b,c,d,e,f,g,h,i,j = lst
x = a + b + c + d + e + f + g + h + i + j
print(lst,", sum:",x)
