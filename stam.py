# Define a dictionary to store usernames and passwords
users = {}
login_attempts = {}

# Decorator function to track login attempts
def track_login_attempts(func):
    def wrapper(username):
        if username not in login_attempts:
            login_attempts[username] = 1
        else:
            login_attempts[username] += 1
        return func(username)
    return wrapper

# Function to register a new user
def register():
    username = input("Enter your username: ")
    # Check if the username already exists
    if username in users:
        print("Username already exists. Please choose another one.")
        return
    password = input("Enter your password: ")
    # Store the username and password in the dictionary
    users[username] = password
    print("Registration successful!")

# Function to log in an existing user
@track_login_attempts
def login(username):
    password = input("Enter your password: ")
    # Check if the username exists and the password matches
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Main function
def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            username = input("Enter your username: ")
            login(username)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
