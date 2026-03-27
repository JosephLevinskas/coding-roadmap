tasks = []

while True:
    print("\n---Task Manager---") #Initial printings
    print("1. View tasks")
    print("2. Add task")
    print("3. Quit")
    
    choice = input("Choose an option: ").strip() #Getting input for choice
    
    if choice == "1": #choice 1 print tasks
        if len(tasks) == 0: #make sure there are tasks
            print("No tasks yet")
        else:
            for i, task in enumerate(tasks, start = 1): #print all tasks
                print(f"{i}. {task}") #use f string here

    elif choice == "2": #Choice 2 add new task
        task = input("Enter a new task: ").strip() #strip white space and get new task input
        if task:
            tasks.append(task) #add task to list
            print("Task added")
        else:
            print("task cannot be nothing") #Checking for empty task input
    
    elif choice == "3": #Choice 3 end session
        print("Goodbye.")
        break #breaks loop

    else: 
        print("Invalid option. Try again.")