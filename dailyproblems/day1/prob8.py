import cmath 
op = input("Operation performing: " )
if op == "+" or op == "-" or op == "*" or op == "/":
    a = input("First complex no:" )
    b = input("Second complex no:"  )
    
    c = complex(a.replace(" ", ""))
    d = complex(b.replace(" ", ""))
    
    if op == "+" :
        print("Sum:", c + d)
    
    elif op == "-" :
        print("Difference:", c - d)
        
    elif op == "*" :
        print("Product:", c * d)

    elif op == "/" :
        print("Quotient:", c / d)

else:
    e = input("Complex Number: ")
    f = complex(e.replace(" ", ""))
        
    if op == "sin" :
        print("Required answer:", cmath.sin(f))
        
    elif op == "cos" :
        print("Required answer:", cmath.cos(f))

    elif op == "tan" :
        print("Required answer:", cmath.tan(f))
            
    elif op == "sqrt":
        print("Required answer:", cmath.sqrt(f))

    elif op == "log":
        print("Required answer:", cmath.log(f))
        
    else:
        print("Required answer:", cmath.exp(f))
