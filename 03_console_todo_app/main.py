memory = {}


def add_task(task_dict: dict) -> None:
    """Prompt the user to enter a new task and add it to the list."""
    while True:
        new_task = input("\nADD NEW TASK: ").upper()
        if new_task.strip() == "":
            print("TASK CANNOT BE EMPTY!")
        else:
            task_id = len(task_dict) + 1
            task_dict[task_id] = new_task
            print("\nNEW TASK ADDED.")
            break


def show_task(task_dict: dict) -> None:
    """Print the current tasks from the list to the console."""
    if len(task_dict) == 0:
        print("\nYOUR TODO LIST IS EMPTY!")
    else:
        print("\n--- CURRENT TASKS ---")
        max_length = 0
        for key, value in task_dict.items():
            print(f"{key}) {value}")
            if len(value) > max_length:
                max_length = len(value)

        print("-" * (max_length + 3))


def delete_task(task_dict: dict) -> None:
    """Prompt the user to enter a task number and delete it from the dictionary."""
    try:
        user_option = int(input("\nWHICH TASK YOU WANT DELETE?: "))
    except ValueError:
        print("\nINVALID INPUT! PLEASE ENTER A NUMBER.")
        return

    if user_option in task_dict:
        del task_dict[user_option]
        print("\nTASK DELETED.")
    else:
        print("\nTASK NOT FOUND.")


while True:
    try:
        menu = int(input("\n1 = ADD TASK, 2 = SHOW TASKS, 3 = DELETE TASK, 4 = EXIT: "))
    except ValueError:
        print("\nINVALID OPTION. PLEASE ENTER A NUMBER.")
        continue

    if menu == 1:
        add_task(memory)
    elif menu == 2:
        show_task(memory)
    elif menu == 3:
        delete_task(memory)
    elif menu == 4:
        print("EXIT..")
        break
    else:
        print("INVALID OPTION. PLEASE CHOOSE 1, 2, 3, OR 4.")
