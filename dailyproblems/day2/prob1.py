
#lst = [1,2,3,5,6]
#Write below code 
#    1) how many elements 
#   2) is 7 part of lst 
#   3) compare with [1,2,3] if same , print "same" else "not-same"
#   4) add 10 to first element and update that value to first element 

lst = [1,2,3,5,6]

print("1) Number of characters:",len(lst))
print("2) Is 7 part of lst:", 7 in lst)

lst2 = [1,2,3]

if lst == lst2:
    print("3) same")
else:
    print("3) not-same")
    
lst[0] += 10
print("4)",lst)


    




