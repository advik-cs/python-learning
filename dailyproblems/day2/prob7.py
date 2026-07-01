#input_str = "Hello world and Hello Earth"
#print frequency of each word 
#H - 2 
#...
#and so on for other words 
    
s = input("Enter your Sentence:")
s1 = s.split()

d = {}
for e in s1:
    if e in d:
        d[e] += 1    
    else:
        d[e] = 1
        
print(d)
        
