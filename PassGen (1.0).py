import secrets
import string

## variables
letters = string.ascii_letters + string.digits + string.punctuation

password = "".join((secrets.choice(letters) for i in range(10)))

f = open("passwords.txt", "a")
f.write(password + "\n")
f.close()

f = open("passwords.txt", "r")
print(f.read())