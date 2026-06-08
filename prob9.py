import math
var1 = input("What do you want to find: " )

if var1 == "v" or "Final velocity" :
    u = int(input("initial velocity(u): " ))
    a = int(input("acceleration (a): " ))
    t = input("time (t)?, Type nil if unkown: " )
    s = input("distance (s)?, Type nil if unkown: ")
    
    if s == "nil":
        ti = int(t)
        v = u + a * ti
        if var1 == "v":
            print("Final velocity (v) is", v)
    
    if s != "nil":
        d = int(s)
        v = math.sqrt(2*a*d + u**2) 
        print("Final velocity (v) is", v)

if var1 == "s" or "distance" :
    tt = int(t)
    s = u*tt + (a*(tt**2))/2
    print("distance moved (s) is", s) 
    
  
    







#v = u + at
#s = ut + 1/2at2
#v2 - u2 = 2as
