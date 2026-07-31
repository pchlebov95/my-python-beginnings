memory = []
star = "* "

while True:
    menu = input("\n1 = ADD TASK, 2 = SHOW TASKS, 3 = EXIT: ")

    if menu == "3":
        print("EXIT...")
        break

    elif menu == "1":
        new_task = input("\nADD NEW TASK: ").upper()
        memory.append(new_task)
        print("\nNEW TASK ADDED.")

    elif menu == "2":
        if len(memory) == 0:
            print("\nYOUR TODO LIST IS EMPTY!")
        else:
            print("\n--- CURRENT TASKS ---")
            for data in memory:
                print(f"{star} {data}")
            print("---------------------")