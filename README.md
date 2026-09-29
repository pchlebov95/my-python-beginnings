**My Python Beginnings 🚀**
Welcome to my repository where I track my Python learning progress. Here are my first 3 mini-projects. All projects focus on clean code and robust input validation.

📁 Project Overview

**1. Password Generator**
   
**Description**: Cryptographically secure terminal password generator.
**Key Features**: Generates unpredictable passwords using secure generation methods and customized character sets.
**Best Practices**: Type hints, PEP 8 styling, Docstrings, .join() optimization, defensive while loops, and robust error handling using try-except blocks to validate user input against empty values, letters, and short lengths.
**Tech Stack**: Python 3, secrets (secure), string.

**QA Manual Testing**: This project has been thoroughly tested using manual QA methodologies, focusing on Boundary Value Analysis for password length restrictions and Equivalence Partitioning for character set validation. 👉 You can find the full test cases and results in the TESTING.md file.

**2. Math Speed Trainer**
    
**Description**: Terminal game that tests your mental math speed and accuracy.
**Key Features**: Time-tracked arithmetic challenges, instant feedback, and score tracking.
**Best Practices**: Type hints, PEP 8 styling, Docstrings, modular code architecture, and robust input validation using try-except blocks to secure user answers against letters and empty inputs.
**Tech Stack**: Python 3, time, random.

**QA Manual Testing**: This project has been thoroughly tested using manual QA methodologies, focusing on Negative Testing for incorrect math inputs and Equivalence Partitioning to validate score tracking accuracy under time constraints. 👉 You can find the full test cases and results in the TESTING.md file.

**3. ToDo List**
    
**Description**: Simple and interactive command-line task management application.
**Key Features**: Task creation with secure chronological ID generation preventing data duplication or overwrite after deletion, task display with adaptive UI dividers, and task deletion.
**Best Practices**: Type hints, PEP 8 styling, Docstrings, modular code architecture, defensive loops for user inputs, and input validation using try-except blocks to secure the menu system and task deletion against string inputs. 
**Tech Stack**: Python 3.

**QA Manual Testing**: This project has been thoroughly tested using manual QA methodologies, including State Transition Testing to evaluate how data deletion impacts dictionary memory, and Negative Testing for empty task inputs. 👉 You can find the full test cases and results in the TESTING.md file.
