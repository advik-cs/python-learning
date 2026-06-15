import math 
op = input("Operation performing: " )
if op == "+" or op == "-" or op == "*" or op == "/":
    one = float(input("First number: "))
    two = float(input("Second number: "))
  
    sum = one + two
    diff = one - two
    product = one * two
    div = one / two
    
    if op == "+" :
        print("Sum:", sum)
    
    elif op == "-" :
        print("Difference:", diff)
        
    elif op == "*" :
        print("Product:", product)

    elif op == "/" :
        print("Quotient:", div)

else:
    e = float(input("Number: "))

    sine = math.sin(e) 
    cosine = math.cos(e)
    tane = math.tan(e)
    sqrtt = math.sqrt(e)
    logg = math.log(e)
    expp = math.exp(e)

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