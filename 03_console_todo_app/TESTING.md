# TC001 - Valid option number 4 (EXIT)

**Pre-condition:**
* The program is running and displaying the main menu.

**Test Steps:**
* Type the number "4" into the terminal.
* Press Enter.

**Expected Result:**
* The program displays the message: "EXIT.."
* The program ends.

# TC002 - Add a new task

**Pre-condition:**
* The program is running and displaying the main menu.

**Test Steps:**
* Type the number "1" into the terminal.
* Press Enter.
* Type the text "buy milk" into the terminal.
* Press Enter.

**Expected Result:**
* The program displays the message: "NEW TASK ADDED."
* The program continues and displays the main menu.

# TC003 - Task ID generation logic

**Pre-condition:**
* The program is running and displaying the main menu.

**Test Steps:**
* Type "1" (ADD TASK) into the terminal and press Enter.
* Type "task a" into the terminal and press Enter.
* Type "1" (ADD TASK) into the terminal and press Enter.
* Type "task b" into the terminal and press Enter.
* Type "3" (DELETE TASK) into the terminal and press Enter.
* Type "1" (to delete ID 1) into the terminal and press Enter.
* Type "1" (ADD TASK) into the terminal and press Enter.
* Type "task c" into the terminal and press Enter.

**Expected Result:**
* "task c" is successfully added as a new task with a new unique ID (ID 3).
* The existing task with ID 2 remains unchanged.

**Status**:
* PASS (Tested after code fix, ID counter now works correctly and no data is overwritten)

# TC004 - Valid option number 2 (SHOW TASKS)

**Pre-condition:**
* The program is running, displaying the main menu, and the todo list is currently empty.

**Test Steps:**
* Type the number "2" (SHOW TASKS) into the terminal.
* Press Enter.

**Expected Result:**
* The program displays the message: "YOUR TODO LIST IS EMPTY!"
* The program continues and displays the main menu.
