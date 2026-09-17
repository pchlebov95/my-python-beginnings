import time
import random

DASH = "-" * 30


def get_user_input(question_text: str) -> int:
    """Get validated integer from user input."""
    while True:
        try:
            return int(input(question_text))
        except ValueError:
            print("INVALID INPUT. PLEASE ENTER A NUMBER.")


def play_round() -> bool:
    """Play one round and return accuracy."""
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    question = f"What is {num1} + {num2}?: "
    user_answer = get_user_input(question)

    if user_answer == num1 + num2:
        print("CORRECT!")
        print(DASH)
        return True
    else:
        print("INCORRECT!")
        print(DASH)
        return False


def main() -> None:
    """Run the game loop and print final stats."""
    print(f"\nWELCOME TO MATH-SPEED-TRAINER!\n{DASH}")
    current_time = time.time()
    score = 0

    for _ in range(5):
        if play_round():
            score += 1
    end_time = time.time()
    total_time = end_time - current_time

    print(f"YOU GOT {score} OUT OF 5 CORRECT ANSWERS.\nTOTAL TIME: {round(total_time)}S")


if __name__ == "__main__":
    main()
