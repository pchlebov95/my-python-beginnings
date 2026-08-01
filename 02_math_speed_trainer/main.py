import time
import random

print("\nWELCOME TO MATH-SPEED-TRAINER!")
print("-" * 30)
current_time = time.time()
score = 0

for i in range(5):
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    while True:
        user_answer = input(f"What is {num1} + {num2}?: ")

        if user_answer.isdigit():
            user_answer_numb = int(user_answer)
            break
        else:
            print("Invalid input. Please enter a number.")

    if user_answer_numb == num1 + num2:
        score += 1
        print("CORRECT!")
        print("--------------------\n")
    else:
        print("INCORRECT!")
        print("--------------------\n")


end_time = time.time()
total_time = end_time - current_time
print(f"YOU GOT {score} OUT OF 5 CORRECT ANSWERS.\nYOUR TIME IS: {round(total_time)}s")
