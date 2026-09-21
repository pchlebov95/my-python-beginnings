# TC001 - Correct answer input

Test Steps:
* Type the correct answer (number 30 for 14 + 16) into the terminal.
* Press Enter.

Expected Result:
* The program displays the message: "CORRECT!"
* The program displays a divider line (dashes).
* The program moves to the next question


# TC002 - Incorrect answer input

Test steps:
* Type the incorrect answer (number 5 for 14 + 16) into the terminal.
* Press Enter

Expected Result:
* The program displays the message: "INCORRECT!"
* The program displays a divider line (dashes).
* The program moves to the next question.


# TC003 - Text input instead  of a number

Test steps:
* Type the text "jedi" into the terminal.
* Press Enter.

Expected Result:
* The program displays the message: "INVALID INPUT. PLEASE ENTER A NUMBER"
* The program repeats the same math question.


# TC004 - Empty input

Test steps:
* Leave the input empty.
* Press Enter

Expected Result:
* The program displays the message: "INVALID INPUT. PLEASE ENTER A NUMBER"
* The program repeats the same math question.


# TC005 - Final statistics with perfect score

Test steps:
* Answer all 5 math questions correctly.
* Press Enter after each answer.

Expected Result:
* The program displays message: "YOU GOT 5 OUT OF 5 CORRECT ANSWERS."
* The program displays the total elapsed time in seconds ("TOTAL TIME: 12S").


# TC006 - Timer calculation with delay

Test steps:
* Start the program.
* Wait 5 seconds before answering the first math question.
* Answer all remaining questions and finish the game.

Expected Result:
* The program finishes and displays the final statistics.
* The total time displays a value greater than 5 seconds ("TOTAL TIME: 6S").