import secrets
import string
import random

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Generate and print a 16-character password
print("Generated Password:", type(generate_password()))
