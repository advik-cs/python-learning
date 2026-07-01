#With knowledge of Set creation
#s = {1,2,3}
#is it same with {3,2,1}, if same print "same" else "no-same"
#print length
#if 30 not part of s, then print "not-part"
#print first element 
#add 10 to each element and print 

s = {1,2,3}
s1 = {3,2,1}

if s == s1:
    print("same")
else:
    print("no-same")
    
print("Length:", len(s))

if 30 not in s:
    print("not-part")

s2 = set()    
for e in s:
    s2.add(e+10)

print(s2)