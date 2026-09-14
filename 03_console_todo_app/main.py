memory = []
STAR = "* "
DASH = "-" * 21


def show_task(task_list: list[str]) -> None:
    """Print the current tasks from the list to the console."""
    if len(task_list) == 0:
        print("\nYOUR TODO LIST IS EMPTY!")
    else:
        print("\n--- CURRENT TASKS ---")

        for data in task_list:
            print(f"{STAR} {data}")

        print(f"{DASH}")


def add_task(task_list: list) -> None:
    """Prompt the user to enter a new task and add it to the list."""
    while True:
        new_task = input("\nADD NEW TASK: ").upper()
        if new_task.strip() == "":
            print("TASK CANNOT BE EMPTY!")
        else:
            task_list.append(new_task)
            print("\nNEW TASK ADDED.")
            break


while True:
    menu = input("\n1 = ADD TASK, 2 = SHOW TASKS, 3 = EXIT: ")
    if menu == "3":
        print("EXIT...")
        break
    elif menu == "1":
        add_task(memory)
    elif menu == "2":
        show_task(memory)
    else:
        print("INVALID OPTION. PLEASE CHOOSE 1, 2, OR 3.")
