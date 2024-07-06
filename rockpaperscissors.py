import random
user_wins=0
bot_wins=0
score=[user_wins,bot_wins]
while 3 not in score:
    choices = ["rock","paper","scissors"]
    r = random.randrange(3)
    bot_choice = choices[r]
    user_choice = input("rock/paper/scissors ?")
    print(user_choice,"x",bot_choice)
    if user_choice not in choices :
        print("You lost, there is no", user_choice, "in this game")
    else:
        if bot_choice == user_choice:
            print("DRAW")
        elif bot_choice == "rock":
            score=[user_wins+1,bot_wins] if user_choice == "paper" else [user_wins,bot_wins+1]
        elif bot_choice == "paper":
            score=[user_wins+1,bot_wins] if user_choice == "scissors" else [user_wins,bot_wins+1]
        elif bot_choice == "scissors":
            score=[user_wins+1,bot_wins] if user_choice == "rock" else [user_wins,bot_wins+1]
        user_wins=score[0]
        bot_wins=score[1]
        print("You:",score[0],"\nBot:",score[1])
if score[0]>score[1]:
    print("Congrats, you won")
else:
    print("Looserrrrr !")