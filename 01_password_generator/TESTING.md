# TC001 - Valid password length input

**Pre-conditions:**
* The program is running and displaying the message: "CHOOSE YOUR PASSWORD LENGTH:"

**Test Steps:**
* Type the number "5" into the terminal.
* Press Enter.

**Expected Result:**
* The program prints a generated password with a length of 5 random characters.
* The program displays a question asking if the user wants to generate another password (Y/N).


# TC002 - Text input instead of a number

**Pre-conditions:**
* The program is running and displaying the message: "CHOOSE YOUR PASSWORD LENGTH:"

**Test Steps:**
* Type the text "ahoj" into the terminal.
* Press Enter.

**Expected Result:**
* The program displays an error message: "INVALID INPUT: PLEASE ENTER A NUMBER"
* The program asks for the password length again.


# TC003 - Float input instead of a number

**Pre-conditions:**
* The program is running and displaying the message: "CHOOSE YOUR PASSWORD LENGTH:"

**Test Steps:**
* Type the float number "5.5" into the terminal.
* Press Enter.

**Expected Result:**
* The program displays an error message: "INVALID INPUT: PLEASE ENTER A NUMBER"
* The program asks for the password length again.


# TC004 - Input length below minimum requirement

**Pre-conditions:**
* The program is running and displaying the message: "CHOOSE YOUR PASSWORD LENGTH:"

**Test Steps:**
* Type the integer number "3" into the terminal.
* Press Enter.

**Expected Result:**
* The program displays an error message: "PASSWORD MUST BE AT LEAST 4 CHARACTERS LONG"
* The program asks for the password length again.


# TC005 - Boundary input at minimum requirement

**Pre-conditions:**
* The program is running and displaying the message: "CHOOSE YOUR PASSWORD LENGTH:"

**Test Steps:**
* Type the integer number "4" into the terminal.
* Press Enter.

**Expected Result:**
* The program prints a generated password with a length of 4 random characters.
* The program displays a question asking if the user wants to generate another password (Y/N).


# TC006 - Empty input

**Pre-conditions:**
* The program is running and displaying the message: "CHOOSE YOUR PASSWORD LENGTH:"

**Test Steps:**
* Leave the input empty.
* Press Enter.

**Expected Result:**
* The program displays an error message: "INVALID INPUT: PLEASE ENTER A NUMBER"
* The program asks for the password length again.


# TC007 - Generate another password with uppercase Y

**Pre-conditions:**
* A password has been generated and the program is displaying a question asking if the user wants to generate another password (Y/N).

**Test Steps:**
* Type the text "Y" into the terminal.
* Press Enter.

**Expected Result:**
* The program converts "Y" into the lowercase "y"
* The program asks for the password length again.


# TC008 - Generate another password with uppercase N

**Pre-conditions:**
* A password has been generated and the program is displaying a question asking if the user wants to generate another password (Y/N).

**Test Steps:**
* Type the text "N" into the terminal.
* Press Enter.

**Expected Result:**
* The program converts "N" into the lowercase "n"
* The program ends.


# TC009 - Typing invalid text instead of Y/N

**Pre-conditions:**
* A password has been generated and the program is displaying a question asking if the user wants to generate another password (Y/N).

**Test Steps:**
* Type the text "karel" into the terminal.
* Press Enter.

**Expected Result:**
* The program ends.
