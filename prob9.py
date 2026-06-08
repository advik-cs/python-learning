var1 = input("What do you want to find?" )



if var1 == "v":
    u = int(input("initial velocity(u)?" ))
    a = int(input("acceleration (a)?" ))
    t = input("time (t)?, Type nil if unkown" )
    s = input("distance (s)?, Type nil if unkown")
    
    if s == "nil":
        ti = int(t)
        v = u + a * ti
        print("Final velocity (v) is", v)
    
    if s != "nil":
        d = int(s)
        v ** 2 - u ** 2 == 2 * a * d 
        print("Final velocity (v) is", v)
    
  
    







#v = u + at
#s = ut + 1/2at2
#v2 - u2 = 2as
