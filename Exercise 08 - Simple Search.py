#creating a list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#asking user to enter a name they are looking for
search_name = input("Enter the name you are looking for: ")

#using if else statement to verify the user's input
if search_name in names:
    print(f"{search_name} It is in the list.")
else:
    print(f"{search_name} It is not found in the list.")
