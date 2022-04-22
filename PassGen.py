import secrets
import string

# Title
print("PassGen" + "\n")

# Customization
Length = int(input("Password Length?\n"))
Name = input(("Text-File Name?\n"))

# Variables
letters = string.ascii_letters + string.digits + string.punctuation



# Password and Exporting
password = "".join((secrets.choice(letters) for i in range(Length)))

o = open(Name + ".txt", "a")
o.write(password + "\n")
o.close()

o = open(Name + ".txt", "r")
print(o.read())