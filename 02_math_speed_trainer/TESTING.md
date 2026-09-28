# TC001 - Correct answer input

**Pre-conditions:**
* The program is running and displaying a math question, for example: "14 + 16 = ".

**Test Steps:**
* Type the correct answer (number 30 for 14 + 16) into the terminal.
* Press Enter.

**Expected Result:**
* The program displays the message: "CORRECT!"
* The program displays a divider line (dashes).
* The program moves to the next question.

# TC002 - Incorrect answer input

**Pre-conditions:**
* The program is running and displaying a math question, for example: "14 + 16 = ".

**Test Steps:**
* Type the incorrect answer (number 5 for 14 + 16) into the terminal.
* Press Enter.

**Expected Result:**
* The program displays the message: "INCORRECT!"
* The program displays a divider line (dashes).
* The program moves to the next question.

# TC003 - Text input instead of a number

**Pre-conditions:**
* The program is running and displaying a math question, for example: "14 + 16 = ".

**Test Steps:**
* Type the text "jedi" into the terminal.
* Press Enter.

**Expected Result:**
* The program displays the message: "INVALID INPUT. PLEASE ENTER A NUMBER"
* The program repeats the same math question.

# TC004 - Empty input

**Pre-conditions:**
* The program is running and displaying a math question, for example: "14 + 16 = ".

**Test Steps:**
* Leave the input empty.
* Press Enter.

**Expected Result:**
* The program displays the message: "INVALID INPUT. PLEASE ENTER A NUMBER"
* The program repeats the same math question.

# TC005 - Final statistics with perfect score

**Pre-conditions:**
* The program is running and the user is on the final math question, having answered all previous questions correctly.

**Test Steps:**
* Answer all 5 math questions correctly.
* Press Enter after each answer.

**Expected Result:**
* The program displays message: "YOU GOT 5 OUT OF 5 CORRECT ANSWERS."
* The program displays the total elapsed time in seconds, such as "TOTAL TIME: 12S".

# TC006 - Timer calculation with delay

**Pre-conditions:**
* The program is ready to be started.

**Test Steps:**
* Start the program.
* Wait 5 seconds before answering the first math question.
* Answer all remaining questions and finish the game.

**Expected Result:**
* The program finishes and displays the final statistics.
* The total time displays a value greater than 5 seconds, such as "TOTAL TIME: 6S".
