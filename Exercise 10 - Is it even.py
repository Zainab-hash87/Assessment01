# Function to determine if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:  # Check if the number is divisible by 2
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

# using Main function
def main():
    while True:
        # Prompt the user to input a number
        user_input = input("Enter a number: ")
        if user_input.lstrip('-').isdigit():  # Check for valid integer input (including negatives)
            number = int(user_input)
            break
        else:
            print("Invalid input. Please enter a valid integer.")

    # Call the check_even_odd function and store the result
    result = check_even_odd(number)
    
    # Print the message returned by the function
    print(result)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
