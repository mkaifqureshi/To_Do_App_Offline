tasks = []


# Load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            data = []
            for line in f.readlines():
                parts = line.strip().split(" | ")
                if len(parts) == 3:
                    task, priority, status = parts
                    data.append({
                        "task": task,
                        "priority": priority,
                        "status": status
                    })
            return data
    except:
        return []


# Save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as f:
        for t in tasks:
            f.write(f"{t['task']} | {t['priority']} | {t['status']}\n")


tasks = load_tasks()

print("Smart To-Do App (Offline)")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Search Task")
    print("5. Exit")

    choice = input("Choose: ")

    # ADD TASK
    if choice == "1":
        task = input("Enter task: ")
        priority = input("Priority (high/medium/low): ")

        tasks.append({
            "task": task,
            "priority": priority,
            "status": "pending"
        })

        save_tasks()
        print("Task Added")

    # VIEW TASKS (SMART SORT)
    elif choice == "2":
        print("\nTASKS (High → Low Priority)\n")

        def priority_value(p):
            if p == "high":
                return 1
            elif p == "medium":
                return 2
            else:
                return 3

        for t in sorted(tasks, key=lambda x: priority_value(x["priority"])):
            print(f"- {t['task']} | {t['priority']} | {t['status']}")

    # MARK DONE
    elif choice == "3":
        for i, t in enumerate(tasks):
            print(i, "-", t["task"], "|", t["status"])

        idx = int(input("Enter task number: "))
        tasks[idx]["status"] = "done"
        save_tasks()
        print("Marked Done")

    # SEARCH
    elif choice == "4":
        query = input("Search task: ").lower()

        found = [t for t in tasks if query in t["task"].lower()]

        if found:
            for t in found:
                print(f"- {t['task']} | {t['priority']} | {t['status']}")
        else:
            print("No tasks found")

    # EXIT
    elif choice == "5":
        break

print("App Closed")
