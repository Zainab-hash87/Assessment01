names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_name = input("Enter the name you are looking for: ")

if search_name in names:
    print(f"{search_name} It is in the list.")
else:
    print(f"{search_name} It is not found in the list.")