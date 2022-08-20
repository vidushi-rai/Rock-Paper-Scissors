import random
user_wins = 0
computer_wins =0
draw=0

options = ["R","P","S"]

while True:
    user_input = input("Type R/P/S or Q to quit: " )
    if user_input == 'Q' :
        break
    
    if user_input not in ['R' , 'P' , 'S']:
        continue

    random_num = random.randint(0,2)
    computer_pick = options[random_num]
    print ("Computer : " , computer_pick)

    if user_input == "R" and computer_pick == "S":
        print ("Victory")
        user_wins +=1
        

    elif user_input == "S" and computer_pick == "P":
        print ("Victory")
        user_wins +=1
        

    elif user_input == "P" and computer_pick == "R":
        print ("Victory")
        user_wins +=1
        
    elif user_input==computer_pick:
        print("Draw")
        draw+=1
        
    else:
        print ("You lost")
        computer_wins +=1

print("You won ", user_wins, "times.")
print("Computer won ", computer_wins, "times.")
print("Match Draw: ",draw)
print("Thanks for playing")


    
