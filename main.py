import time
import random

print("WELCOME TO MATH-SPEED-TRAINER!\n")
current_time = time.time()
score = 0

for i in range(5):
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    user_answer = int(input(f"What is {num1} + {num2}?: "))

    if user_answer == num1 + num2:
        score += 1
        print("CORRECT!")
        print("--------------------\n")
    else:
        print("INCORRECT!")
        print("--------------------\n")


end_time = time.time()
total_time = end_time - current_time
print(f"YOU GOT {score} OUT OF 5 CORRECT ANSWERS.\nYOUR TIME IS: {round(total_time)}s")
