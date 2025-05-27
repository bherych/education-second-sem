import avl_priority_queue as queue

start_program = input("Do you want to start to-do helper? Y/N: ")

if start_program.lower() == "y" or "yes":
    command_helper = "List of Commands:\n " \
    "exit - to exit an application\n" \
    "help - to view command list again\n" \
    "add - to add new task to the list\n" \
    "done - removes a task with highest priority\n" \
    "show - shows a list of all current tasks"
    
    print(command_helper)

    pq = queue.PriorityQueueAVL()

    while True:
        user_input = input("Enter a command: ")
        match user_input:
            case "exit":
                break
            case "help":
                print(command_helper)
                continue
            case "add":
                task = input("Enter a content of a task: ")
                priority = int(input("Enter a number for priority of this task: "))
                print(priority)

                pq.insert(priority=priority, value=task)

                continue

            case "show":
                pq.print_queue()
            
            case "done":
                task_done = pq.pop()
                print("Removed '{task}' from the list")
                continue
