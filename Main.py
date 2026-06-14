import random
x = random.randint(1, 10)
tries = 0
while True:
    a = input("Guess the number between 1 to 10: ")
    
    if a.isdigit():
        tries += 1
        
        if int(a) == x:
            print("You win\nYou are genius")
            break
            
        elif int(a) > x:
            print("You lose \nTry again...\nChoose lower number")
        else:  # a < x
            print("You lose \nTry again...\nChoose higher  number ") 
        if tries==7:
            print (" Game over, the number was:",x)
            break 
            
    else:  
        print("Invalid entry ,Try again..")
print("Total tries:", tries)
