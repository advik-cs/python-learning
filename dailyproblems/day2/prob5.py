#Given input, Write code to get output 
#input = "aaabbbbaaac"
#output = "abc"

a = "aaabbbbaaac"
b = ""
for char in a:
    if char not in b:
        b = b + char
        
print(b)