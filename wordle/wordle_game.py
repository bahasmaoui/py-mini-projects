#libraries
import random
import time

#used functions
def show(guess):
    ch=""
    for x in guess:
        ch += x.upper()+" "
    return ch
def compare(guess,word):
    used_indices = set()
    l=["-"]*len(word)
    #check for correct pos/correct letter:
    for i in range(len(word)):
        if guess[i] == word[i] :
            l[i]="G"
            used_indices.add(i)
    #check for correct letter/wrong pos
    for i in range(len(word)):
        if guess[i] in word and not(i in used_indices) :
            l[i]="Y"
            used_indices.add(i)
    #check gray letters
    for x in guess :
        if not x in word :
            gray_letters.add(x)
            
    return show(l)

def gameplay(max_letters,words):
    global gray_letters
    word = random.choice(words)
    guesses = 1
    gray_letters=set()
    while True:
        guess = input(f"Guess {guesses} {sorted(gray_letters)}\n   ->")
        while len(guess) != len(word):
            guess = input("Guess "+str(guesses)+"\n   ->")
        print(show(guess))
        print(compare(guess,word))
        guesses += 1
        if guesses > 7 :
            print(f"Out of Guesses \n The word was '{show(word)}'")
            ans = input("[play] another round/\n[change] Game settings\n (click anything to quit)")
            while ans in ["play","change"]:
                if ans == "play":
                    gameplay(len(word),words)
                elif ans == "change":
                    nb_letters,words=set_game()
            gameplay(nb_letters,words)
            quit()
        elif word == guess :
            print(f"Congrats, you guessed '{show(word)}' correctly in {guesses} guesses!")
            ans = input("[play] another round/\n[change] Game settings\n (click anything to quit)")
            while ans in ["play","change"]:
                if ans == "play":
                    gameplay(nb_letters,words)
                elif ans == "change":
                    nb_letters,words=set_game()
                    gameplay(nb_letters,words)
            print(f"Goodbye {name}")
            quit()
def extract(file_name):
    with open(file_name,'r') as file:
        words = [line.strip() for line in file.readlines() if line.strip()]
    return words
def number_to_text(nb):
    l=["THREE","FOUR","FIVE","SIX","SEVEN"]
    return l[nb-3]
def set_game():
    nb_letters = input("Number of letters [3,7]: (click anything for random number)")
    if nb_letters not in ["3","4","5","6","7"]:
        nb_letters=str(random.randint(3,7))
    file_name = f"wordle_{nb_letters}_letters.txt"
    words=extract(file_name)
    return nb_letters,words
#start of the game
print("WORDLE")
time.sleep(1)
print("Welcome to WORDLE in python")
time.sleep(1)
name=input("First what's your name? ")
time.sleep(1)
print(f"Hello {name.upper()}, let's set up your first game!")
print("---------------------------------")
time.sleep(1)
print("GAME SETTINGS")
nb_letters,words=set_game()
print(f"NUMBER: {nb_letters}")
print("---------------------------------")
print("The rules are simple")
time.sleep(1)
print(f"The goal here is to guess the {number_to_text(int(nb_letters))}-letters word in less than 7 guesses")
time.sleep(2)
print("The code will let you know if letters are correct")
time.sleep(2)
print("and/or correctly placed.")
time.sleep(1.5)
print("Also, the letters that are neither correct and/or correctly placed")
time.sleep(2)
print("Will be next to your guess")
time.sleep(1.5)
print("Let the game begin")
gameplay(nb_letters,words)
