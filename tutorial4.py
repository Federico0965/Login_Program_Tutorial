# STEP 0: MAKE A DICTIONARY TO STORE OUR USERS
users = {}
passwords = {}

# STEP 1: FUNCTION TO SIGN UP AND LOGIN
def register_account():
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    print("Success: Account created.")
    print("-------------------------")
    users[username] = password
    passwords[password] = username

def login():
    print(users)
    print(passwords)
    ask_username = str(input("Username: "))
    ask_password = str(input("Password: "))
    if ask_username in users:
        if ask_password in passwords:
            print("Success: You have logged in.")
            print("----------------------------")
    if ask_username not in users:
        if ask_password not in passwords:
            print("Error: Login failed.")
            print("--------------------")

# STEP 2: DEFINE THE MAIN FUNCTION
def main():
    while True:
        print("LOGIN PROGRAM")
        print("-------------")
        print("Choose an option:")
        print("(1) Create an account\n(2) Login\n(3) Exit")
        choice = input("Type the option number: ")
        if choice == "1":
            register_account()
        elif choice == "2":
            login()
        elif choice == "3":
            break

# STEP 3: RUN THE PROGRAM
main()
