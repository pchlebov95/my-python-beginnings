import string
import secrets

def generate_length_password() -> int:
    """
    Ask the user for a password length and validate it.  
    """

    while True:
        password_length = input("\nChoose your password length: ")

        if password_length.isdigit():
            password_length_numb = int(password_length)

            if password_length_numb >= 4:
                return password_length_numb
            else:
                print("Password must be at least 4 characters long")

        else:
            print("Invalid input: Please enter a number.")


def create_password(length: int) -> str:
    """
    Create a secure password from letters, digits, and punctuation.
    """

    all_characters = string.ascii_letters + string.digits + string.punctuation
    password_chars = []

    for _ in range(length):
        random_char = secrets.choice(all_characters)
        password_chars.append(random_char)

    return ''.join(password_chars)

if __name__ == "__main__":
    while True:
        result_length = generate_length_password()
        complete_password = create_password(result_length)

        print(f"Generated password: {complete_password}")
        user_choice = input("Generate another password? (y/n): ").lower().strip()

        if user_choice != "y":
            break
