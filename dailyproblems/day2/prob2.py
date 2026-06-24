#lst = ["OK", "NOK", "hello", "hi"]
#Write below code 
#    4) print last element, 2nd last and first element ,
#        Update last element to "hello"
#    5) what is length of 2nd element string 
#    6) print first two , last two elements 
#    7) print reverse of last 
#    8) print every 2nd element 
#    9) print every element 
#    10) print every element's length 

lst = ["OK", "NOK", "hello", "hi"]
print(lst[-1], lst[-2], lst[0])

lst[-1] = "hello"

print(len(lst[1]))
 
print(lst[0], lst[1], lst[-1], lst[-2])

a = lst[-1]
print(a[-1::-1])

print(lst[1], lst[3])

print(lst[0], lst[1], lst[2], lst[3])

print(len(lst[0]),len(lst[1]),len(lst[2]),len(lst[3]))



