s = input("Enter your Sentence:")
s1 = s.split()

d = {}
for e in s1:
    if e in d:
        d[e] += 1    
    else:
        d[e] = 1
        
print(d)
        