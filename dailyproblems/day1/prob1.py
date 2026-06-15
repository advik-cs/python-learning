a = input("1st number:" )
b = input("2nd number:" )
c = input("operation:" )

d = float(a)
e = float(b)

sum = d + e
diff = d - e  
product = d * e 
division = d / e  

if c == "+" :
    print(sum)
elif c == "-" :
    print(diff)
elif c == "*" :
    print(product)
elif c == "/" :
    print(division)
    