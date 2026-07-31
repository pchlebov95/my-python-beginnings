import string, random

all_characters = string.ascii_letters + string.digits + string.punctuation
generated_password = ""

password_length = int(input("Choose your password length: "))

for i in range(password_length):
    random_char = random.choice(all_characters)
    generated_password += random_char

print(f"Your new generated password: {generated_password}")