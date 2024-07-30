# Username and Password lists
usernames = ['Arun', 'Mani']
passwords = ['123', '135']

def create_account():
    while True:
        new_username = input("New Username: ")
        if new_username in usernames:
            print("Username already taken")
            continue
        new_password = input("New Password: ")
        while True:
            confirm_password = input("Confirm Password: ")
            if new_password == confirm_password:
               usernames.append(new_username)
               passwords.append(new_password)
               print("Account Created Successfully")
               break
            else:
               print("Error: Confirm Password not Same.")
        main()
def login():
    attempts = 4
    
    while True:
        username = input("Username: ")
        
        if username in usernames:
            print("Username Exists")
            correct_password = passwords[usernames.index(username)]
            
            while attempts > 0:
                password = input("Password: ")
                
                if password == correct_password:
                    print("Login Successful")
                    return
                else:
                    attempts -= 1
                    print('Login Error: Incorrect Password')
                    if attempts > 0:
                        print(f"You have {attempts} attempts left")
                    else:
                        print(f"{username}'s Account Locked")
                        return
        else:
            print("Invalid Username")

# Main function
def main():
    while True:
        choice = input("Login or Create Account: ")
        
        if choice == "Create Account":
            create_account()
        elif choice == "Login":
            login()
        else:
            print("Invalid choice. Please type 'Login' or 'Create Account'.")

# Run the main function
main()
