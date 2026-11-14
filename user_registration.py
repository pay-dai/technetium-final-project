def user_registration(username, password, users):
""" 
Summary: Takes in a username and password from the player and stores their information in the "users" dictionary.

Args:
  username (str): The username chosen by the player
  password (str): The password chosen by the player
  users (dict): Dictionary containing user's registration information and their stats

Mutates:
  users(dict): Stores the new user profile including their: Username, Password, Score, Game Play, and Wins
"""
    while True:
        if len(username) < 4:
            print("Username must be at least 4 characters.")
            username = input("Enter a new username: ")

        else:
            username_taken = False

            for existing_username in users:
                if existing_username.lower() == username.lower():
                    username_taken = True
                    break

            if username_taken:
                print("Username is already taken.")
                username = input("Enter a new username: ")
            else:
                break

    while len(password) < 8:
        print("Password must be at least 8 characters.")
        password = input("Enter a new password: ")

    users[username] = {
        "Password": password,
        "Score": 0,
        "Game Play": 0,
        "Wins": 0
    }

    print("Account has been created!")

   
