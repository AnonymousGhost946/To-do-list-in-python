from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Get user input for the name
name = input(Fore.RED + "Please enter your Full Name: ")

print(Fore.GREEN + f"Welcome, {name}\n")

# Initialize the list
mylist = []

# Function to display the list
def disList():
    listDis = input(Fore.BLUE + "Do you want to see your Goal List (Yes/No): ").lower()
    if listDis == 'yes':
        print(Fore.YELLOW + "\nYour Goal List:")
        for i, k in enumerate(mylist):
            print(Fore.CYAN + f"{i + 1}. {k}")
    else:
        print(Fore.MAGENTA + "Good Luck with your Goals!\n")

# Function to add single or multiple tasks
def addMultiTask():
    taskLen = int(input(Fore.BLUE + "Do you want to add one Task or Multiple Tasks? \nPress 1 to add one task and press 2 to add multiple tasks: "))
    if taskLen == 1:
        singleTask = input(Fore.CYAN + "Enter your first task: ")
        mylist.append(singleTask)
        print(Fore.GREEN + "Task added successfully!\n")
    elif taskLen == 2:
        ask = int(input(Fore.CYAN + "How many tasks do you want to add? "))
        for i in range(ask):
            tasks = input(Fore.YELLOW + f"Enter task {i + 1}: ")
            mylist.append(tasks)
        print(Fore.GREEN + "All tasks added successfully!\n")
    else:
        print(Fore.RED + "Invalid choice. Please try again.\n")

# Function to delete tasks
def delTask():
    askDel = input(Fore.BLUE + "Do you want to delete any task (Yes/No): ").lower()
    if askDel == 'yes':
        print(Fore.YELLOW + f"\nCurrent Goal List: {mylist}\n")
        delitem = input(Fore.CYAN + "Enter the task name you want to delete: ")
        if delitem in mylist:
            mylist.remove(delitem)
            print(Fore.GREEN + f"Task '{delitem}' deleted successfully!\n")
            print(Fore.YELLOW + "This is your updated list: ", mylist)
        else:
            print(Fore.RED + f"Task '{delitem}' not found in the list.\n")
    else:
        print(Fore.MAGENTA + "Good Luck with your Goals!\n")

# Main function to call all tasks
def mainTask():
    addMultiTask()
    disList()
    delTask()
    disList()

# Run the main task
mainTask()
