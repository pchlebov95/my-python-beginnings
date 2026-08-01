# My Python Beginnings 🚀

Welcome to my repository where I track my Python learning progress. Here are my first 3 mini-projects from my 6th week of studying. All projects have been refactored to clean code and include robust input validation to prevent crashes.

## 📁 Project Overview

### 1. Password Generator (v2.0)
* **Description:** A secure tool for generating random passwords.
* **Key Features:** Robust input validation using `.isdigit()` to handle invalid characters, negative numbers, or short password lengths (minimum 4 characters). Clean code with string/random modules.

### 2. Math Speed Trainer (v2.0)
* **Description:** A terminal game that tests your math speed and accuracy under a time limit.
* **Key Features:** Uses nested `while True` loops inside a `for` loop to handle user input securely. If the user makes a typo, the program doesn't crash but prompts for the answer again without resetting progress.

### 3. ToDo List (v2.0)
* **Description:** A simple command-line task management application.
* **Key Features:** Features a secure menu system (handles invalid choices gracefully). Includes data validation with `.strip()` to prevent users from adding blank tasks or empty spaces.
