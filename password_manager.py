import pickle
def add():
    with open("passwords_list.dat","rb") as file:
        apps = pickle.load(file)
    pwd = {}
    app = input("App: ").lower()
    pwd = {"username": input("Username: "), "password": input("Password: ")}
    if app in apps :
        apps[app].append(pwd)

    else:
        apps[app]=[pwd]
    with open('passwords_list.dat', 'wb') as file:
        pickle.dump(apps,file)
    print(app,"password added sucessfully")
    menu()
def show(l):
    for pwd in l:
        print(".  USERNAME: ",pwd["username"])
        print("   PASSWORD: ",pwd["password"])
    print()     
def view():
    try:
        file = open("passwords_list.dat","rb")
        apps = pickle.load(file)
    except:
        ans = input("No Passwords \n Add a new password? \n ->")
        if ans == "yes":
            add()
        else:
            menu()
            return
    apps_keys=list(apps.keys())
    user_choice = input("View All/View Specific App \n ->")
    if user_choice == "all":
        for x in apps_keys :
            if x!="master":
                print(x)
                show(apps[x])
    else:
        print(apps_keys)
        user_choice = input("APP:")
        while not(user_choice in apps_keys):
            user_choice = input("Sorry, this app doesn't exist \n APP:")
        show(apps[user_choice])
    menu()
def menu():
    choice = input("Do you want to \n 1.Add a New Password \n 2.View existing passwords \n ->")
    if choice in ["add", "1"]:
        add()
    elif choice in ["view", "2"]:
        view()
    else:
        quit()
def check_pwd(apps):
    pwd = input("What is the master Password?")
    tries = 0
    while tries <=5 and pwd != apps["master"]["pwd"]:
        pwd = input("Wrong Password ! \n Try again \n ->")
        tries += 1
    if pwd == apps ["master"]["pwd"]:
        print("Welcome")
    else:
        user_choice = input("Forget password ? (y/n)")
        if user_choice == "y":
            forget_answer = input(apps["master"]["question"]+" ?")
            if forget_answer != apps["master"]["answer"] :
                print("Failed to login")
                login()
            else:
                apps["master"]["pwd"] = input("Change Password \n New Master Password:")
                with open("passwords_list.dat","wb") as file:
                    pickle.dump(apps,file)
def create_master_pwd():
    master={}
    master["pwd"] = input("Create a Master Password:")
    master["question"] = input("Choose a question:")
    master["answer"] = input("Answer:")
    return master
def login():
    try:
        with open("passwords_list.dat","rb") as file:
            apps = pickle.load(file)
    except:
        apps = {}
    apps_list = list(apps.keys())
    if "master" in apps_list :
        check_pwd(apps)
    else:
        master=create_master_pwd()
        apps["master"]=master
        print(apps)
        with open("passwords_list.dat","wb") as file:
            pickle.dump(apps,file)
    
#pp  
login()
menu()

