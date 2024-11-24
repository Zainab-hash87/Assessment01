name= input ("Enter full name:")
hometown = input ("Enter hometown:")

while True:
    Age = input ("Enter age:")
    if Age. isdigit():
        age= int(Age)
        break
    else :
        print("Wrong age. Enter age in number")

print(f"Name: {name}")
print(f"Hometown: {hometown}")
print(f"Age: {age}")