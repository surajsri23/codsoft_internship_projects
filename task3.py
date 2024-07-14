import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    if length < 6:
        print("Password length should be at least 8 characters.")
        return None
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password

length = int(input("Enter the desired length of the password: "))
print("Generated Password:", generate_password(length))
