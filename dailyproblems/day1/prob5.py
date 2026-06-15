a = input("First complex no:" )
b = input("Second complex no:"  )
x = input("Operation:" )

c = complex(a.replace(" ", ""))
d = complex(b.replace(" ", ""))

sum = c + d 
diff = c - d 
product = c * d 
division = c / d 

if x == "+":
    print(sum)
if x == "-":
    print(diff)
if x == "*" :
    print(product)
if x == "/" :
    print(division)  
