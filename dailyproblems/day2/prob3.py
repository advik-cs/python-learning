#Create a list of 10 random numbers between 10 and 50 
#Then sum those 
#then print that list and its sum 
import random

lst = [1,1,1,1,1,1,1,1,1,1]
for e in range(0,10,1):
    lst[e] = random.randint(10,50)
    
x = lst[0] + lst[1] + lst[2] + lst[3] + lst[4] + lst[5] + lst[6] + lst[7] + lst[8] + lst[9]

print(lst,", sum:",x)
