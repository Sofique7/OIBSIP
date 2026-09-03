import random
import string

print("===== Random Password Generator =====")

length = int(input("Enter password length: "))

if length < 4:
    print("Password length should be at least 4.")
else:
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ''.join(random.choice(characters) for _ in range(length))

    print("Generated Password:", password)