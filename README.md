My Python Beginnings 🚀
Welcome to my repository where I track my Python learning progress. Here are my first 3 mini-projects. All projects focus on clean code and robust input validation.

📁 Project Overview

1. Password Generator
   
Description: Cryptographically secure terminal password generator.
Key Features: Generates unpredictable passwords using secure generation methods and customized character sets.
Best Practices: Type hints, PEP 8 styling, Docstrings, .join() optimization, defensive while loops, and robust error handling using try-except blocks to validate user input against empty values, letters, and short lengths.
Tech Stack: Python 3, secrets (secure), string.

3. Math Speed Trainer
    
Description: Terminal game that tests your mental math speed and accuracy.
Key Features: Time-tracked arithmetic challenges, instant feedback, and score tracking.
Best Practices: Type hints, PEP 8 styling, Docstrings, modular code architecture, and robust input validation using try-except blocks to secure user answers against letters and empty inputs.
Tech Stack: Python 3, time, random.

3. ToDo List
    
Description: A simple command-line task management application.
Key Features: Task creation, display, and deletion via an interactive command-line interface.
Improvements: Refactored core storage from list to dict, added a functional task deletion system via numerical IDs, integrated dynamic task numbering, and implemented clean dictionary unpacking with complete docstrings and type hints. Integrated robust error handling using try-except blocks to completely secure the menu system and task deletion against invalid inputs like letters. Replaced hardcoded UI dividers with a dynamic dash separator that automatically calculates and adjusts its length based on the longest task in the list to prevent visual breaking.
Best Practices: Code split into modular functions for better structure, strict PEP 8 spacing compliance, secure menu system that handles invalid choices gracefully, data validation with .strip() to prevent blank tasks, and edge-case validation against invalid IDs and non-integer inputs.
Tech Stack: Python 3.
