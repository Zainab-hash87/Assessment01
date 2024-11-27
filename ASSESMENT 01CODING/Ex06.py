#declaring the correct password
correct_password = "12345"
max_attempts = 5
attempts = 0      #initial attempts 

while attempts < max_attempts:
    password = input("Enter the password: ")     #asking user to enter their password
    
#using if else statement to check the password 
    if password == correct_password:
        print("Signed in!")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts    #this will display the remaining attempts left
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("The authorities have been alerted.")
