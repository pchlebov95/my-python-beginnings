memory = []
star = "* "

while True:
    menu = input("\n1 = ADD TASK, 2 = SHOW TASKS, 3 = EXIT: ")

    if menu == "3":
        print("EXIT...")
        break

    elif menu == "1":

        while True:
            new_task = input("\nADD NEW TASK: ").upper()

            if new_task.strip() == "":
                print("TASK CANNOT BE EMPTY!")
            else:
                memory.append(new_task)
                print("\nNEW TASK ADDED.")
                break

    elif menu == "2":
        if len(memory) == 0:
            print("\nYOUR TODO LIST IS EMPTY!")
        else:
            print("\n--- CURRENT TASKS ---")
            for data in memory:
                print(f"{star} {data}")
            print("---------------------")

    else:
        print("INVALID OPTION. PLEASE CHOOSE 1, 2, OR 3.")
