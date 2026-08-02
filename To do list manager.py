# --- Load previous tasks if file exists ---
try:
    with open("tasks.txt", "r") as f:
        t = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    t = []  # if file doesn't exist yet

# --- Function to save tasks ---
def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in t:
            f.write(task + "\n")


while True:
    print("1: Add Task \n2: View Task\n3: Edit Task\n4: Delete Task\n5: Exit")
    a = int(input("Enter your choice: "))

    if a == 1:
        b = input("Enter task: ")
        t.append(b)
        save_tasks()  # ✅ Save after adding
        print("Task added!")

    elif a == 2:
        print("\nYour Tasks:")
        for i, task in enumerate(t, start=1):
            print(f"{i}. {task}")

    elif a == 3:
        for i, task in enumerate(t, start=1):
            print(f"{i}. {task}")
        choice = int(input("Enter task number to be edited: "))
        new = input("Enter new task: ")
        if 1 <= choice <= len(t):
            t[choice - 1] = new
            save_tasks()  # ✅ Save after editing
            print("Task updated!")
        else:
            print("Invalid task number.")

    elif a == 4:
        for i, task in enumerate(t, start=1):
            print(f"{i}. {task}")
        try:
            r = int(input("Enter task number to remove: "))
            if 1 <= r <= len(t):
                removed = t.pop(r - 1)
                save_tasks()  # ✅ Save after deleting
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input.")

    elif a == 5:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice.")

       