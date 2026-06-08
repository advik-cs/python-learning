import cmath 
op = input("Operation performing: " )
if op == "+" or op == "-" or op == "*" or op == "/":
    a = input("First complex no:" )
    b = input("Second complex no:"  )
    
    c = complex(a.replace(" ", ""))
    d = complex(b.replace(" ", ""))
    
    sum = c + d
    diff = c - d
    product = c * d
    div = c / d
    
    if op == "+" :
        print("Sum:", sum)
    
    elif op == "-" :
        print("Difference:", diff)
        
    elif op == "*" :
        print("Product:", product)

    elif op == "/" :
        print("Quotient:", div)

else:
    e = input("Complex Number: ")
    f = complex(e.replace(" ", ""))
    sine = cmath.sin(f) 
    cosine = cmath.cos(f)
    tane = cmath.tan(f)
    sqrtt = cmath.sqrt(f)
    logg = cmath.log(f)
    expp = cmath.exp(f)
        
    if op == "sin" :
        print("Required answer:", sine)
        
    elif op == "cos" :
        print("Required answer:", cosine)

    elif op == "tan" :
        print("Required answer:", tane)
            
    elif op == "sqrt":
        print("Required answer:", sqrtt)

    elif op == "log":
        print("Required answer:", logg)
        
    else:
        print("Required answer:", expp)
