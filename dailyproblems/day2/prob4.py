#lst = ["OK", "NOK", "hello", "hi"]
#How many even length string and how many odd length string 
#What is the total length of all strings 

lst = ["OK", "NOK", "hello", "hi"]
a = len(lst[0]) 
b = len(lst[1])
c = len(lst[2])
d = len(lst[3])

even = 0
odd = 0

if a%2 == 0:
    even += 1
elif a%2 != 0:
    odd += 1

if b%2 == 0:
    even += 1
elif b%2 != 0:
    odd += 1
    
if c%2 == 0:
    even += 1
elif c%2 != 0:
    odd += 1
    
if d%2 == 0:
    even += 1
elif d%2 != 0:
    odd += 1
    
print("Even Length String:",even,", Odd Length String:",odd)

x = a + b + c + d
print("Total length of strings in list:",x)

    

