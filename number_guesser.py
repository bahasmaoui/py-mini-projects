import random
import math
r = random.randrange(100)
print(r)
tries = 0
try0 = int(input("Choose A number between -5 and 10 "))
while try0 != r:
    d = abs(r-try0)
    if d > 50 :
        closeness = "Freezing"
    elif d > 25 :
        closeness = "Cold"
    elif d > 10 :
        closeness = "Warm"
    elif d > 5 :
        closeness = "Hot"
    elif d > 1 :
        closeness = "Extremely Hot"
    else :
        closeness = "Just once again !"
        if tries == 0:
            print("Dude, almost there")
    print(closeness)
    try0= int(input("Try again! "))
    tries += 1
print("Good Job, The number was",r," \n You guessed it in", tries, "tries")
    