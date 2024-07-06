#questions init
questions = [
    "What is the name of Hagrid's pet dragon in 'Harry Potter and the Philosopher's Stone'? ",
    "Which ghost haunts the girls' bathroom on the second floor of Hogwarts?",
    "What spell does Hermione use to fix Harry's glasses in 'Harry Potter and the Chamber of Secrets'?",
    "Who is the Half-Blood Prince?",
    "What magical creature is Buckbeak?"]
choices = [
        ["Norbert", "Smaug", "Toothless"],
        ["Nearly Headless Nick", "Moaning Myrtle", "The Grey Lady"],
        ["Reparo", "Lumos", "Alohomora"],
        ["Severus Snape", "Tom Riddle", "Sirius Black"],
        ["Phoenix", "Thestral","Hippogriff"],
        
    ]
answers = ["A", "B", "A", "A", "C"]

#starting
print("Welcome to the Ultimate Hogwarts Trivia Challenge!")
print("Step into the magical world of Harry Potter with our enchanting quiz adventure.")
print("Test your wizarding knowledge across ten spellbinding questions covering everything from magical creatures to famous spells.")

playing = input("Start the game?")
if playing != "yes":
    quit()
else:
    points=0
    for i in range(5):
        print("\n STATUS:",points,"POINTS \n")
        print(questions[i])
        for j in range(3):
            print(chr(65+j)+")"+choices[i][j])
        ans=input("\n Answer ")
        if ans==answers[i]:
            print("\n Good Job! +1Point ")
            points+=1
        else:
            print("\n Oops!")
    print("You have", points, "Points !")
    
                
        