#ask user to guess a number from 1 to 100 not including 100 
#Then randomly guess a number in code from 1 to 100 
#if user number is less than code's number , then score is -1 
#if user number is equal to  code's number , then 3
#if user number is greater than code's number , then 1

#Play 10 times and sum of all scores, if it +, then user wins 
#if it is -ive, then code wins 
#Declare the winner

import random
score = 0

for i in range(0,10,1):
    lst = [int(input("Guess a number:" )),random.randint(1,99)]
    a,b = lst
    print(lst)
    
    if a < b:
        score += -1
        
    elif a == b:
        score += 3
        
    else:
        score += 1
        
    print("Current score:", score)
    
print("Final score:", score)

if score > 0:
    print("You win!")    
else:
    print("Code wins")
    