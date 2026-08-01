import string
import random

all_characters = string.ascii_letters + string.digits + string.punctuation
generated_password = ""

while True:
    password_length = input("\nChoose your password length: ")

    if password_length.isdigit():
        password_length_numb = int(password_length)

        if password_length_numb >= 4:
            break
        else:
            print("Password must be a at least 4 characters long")

    else:
        print("Invalid input. Please enter a number.")


for i in range(password_length_numb):
    random_char = random.choice(all_characters)
    generated_password += random_char

print(f"Your new generated password: {generated_password}")
