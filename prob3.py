for i in range(2,101,1):
    prime = True

    for j in range(2,i,1): 
        if i%j == 0:
            prime = False
            
    if prime == True:
        print(i)
    
     