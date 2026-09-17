import secrets
import string

ALLOWED_CHARACTERS = string.ascii_letters + string.digits + string.punctuation


def generate_length_password() -> int:
    """Ask the user for a password length and validate it."""
    while True:
        try:
            password_length = int(input("\nCHOOSE YOUR PASSWORD LENGTH: "))

            if password_length >= 4:
                return password_length
            else:
                print("PASSWORD MUST BE AT LEAST 4 CHARACTERS LONG")

        except ValueError:
            print("INVALID INPUT. PLEASE ENTER A NUMBER.")


def create_password(length: int) -> str:
    """Create a secure password from letters, digits, and punctuation."""
    password_chars = []

    for _ in range(length):
        random_char = secrets.choice(ALLOWED_CHARACTERS)
        password_chars.append(random_char)

    return "".join(password_chars)


if __name__ == "__main__":
    while True:
        result_length = generate_length_password()
        complete_password = create_password(result_length)

        print(f"GENERATED PASSWORD: {complete_password}")
        user_choice = input("GENERATE ANOTHER PASSWORD? (Y/N): ").lower().strip()

        if user_choice != "y":
            break
