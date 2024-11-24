correct_password = "12345"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    password = input("Enter the password: ")
    
    if password == correct_password:
        print("Signed in!")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("The authorities have been alerted.")