import random

a = 0
b = 0

for i in range(0,10000,1):
    input("Player 1: press enter")
    dice1 = random.randint(1,6)
    print("Player 1 rolled: ", dice1)
    a = a + dice1

    if a == 1:
        a += 37
        
    elif a == 4:
        a += 10

    elif a == 9:
        a += 21

    elif a == 16:
        a -= 10

    elif a == 21:
        a += 21

    elif a == 28:
        a += 56

    elif a == 36:
        a += 8
        
    elif a == 47:
        a -= 21
        
    elif a == 49:
        a -= 38
        
    elif a == 51:
        a += 16
        
    elif a == 56:
        a -= 3

    elif a == 62:
        a -= 43
        
    elif a == 64:
        a -= 4
        
    elif a == 71:
        a += 20
        
    elif a == 80:
        a += 20
        
    elif a == 87:
        a -= 63
        
    elif a == 93:
        a -= 20
        
    elif a == 95:
        a -= 20
        
    elif a == 98:
        a -= 20

    print("Player 1 is now at: ", a)
    if a >= 100:
        print("Player 1 wins")
        break

    import random
    input("Player 2: press enter")
    dice2 = random.randint(1,6)
    print("Player 2 rolled:", dice2)
    b = b + dice2

    if b == 1:
        b += 37
        
    elif b == 4:
        b += 10

    elif b == 9:
        b += 21

    elif b == 16:
        b -= 10

    elif b == 21:
        b += 21

    elif b == 28:
        b += 56

    elif b == 36:
        b += 8
        
    elif b == 47:
        b -= 21
        
    elif b == 49:
        b -= 38
        
    elif b == 51:
        b += 16
        
    elif b == 56:
        b -= 3

    elif b == 62:
        b -= 43
        
    elif b == 64:
        b -= 4
        
    elif b == 71:
        b += 20
        
    elif b == 80:
        b += 20
        
    elif b == 87:
        b -= 63
        
    elif b == 93:
        b -= 20
        
    elif b == 95:
        b -= 20
      
    elif b == 98:
        b -= 20

    print("Player 2 is now at: ", b)
    if b >= 100:
        print("Player 2 wins")
        break