import os

#  Command to clear the console
clear_cmd = "clear"
if os.name in ('nt', 'dos'):
    clear_cmd = 'cls'
    
#  Load previous data
if os.path.exists("todos.txt"):
    with open("todos.txt", "r") as f:
        todos = []
        saved_todos = f.readlines()
        for saved_todo in saved_todos:
            saved_todo = saved_todo.replace("\n", "")
            todos.append(saved_todo)
else:
    with open("todos.txt", "w") as f:
        f.write("Water flowers\n")
        todos = ["Water flowers"]

error = None


while True:

    #  Clear the console
    os.system(clear_cmd)
      
    #  Print main text
    print("""\n> SIMPLE TO-DO LIST 
    
> Add a todo: add <TODO TEXT>
> Remove a todo: rem <TODO NUMBER>
 \n""")
    
    #  Print tasks
    for index, todo in enumerate(todos):
        print("  ",(index + 1), "- ", todo, sep='')
    else:
        print("\n")
    
    #  Errors
    if error is not None:
        print("ERROR:", error, "\n")
        error = None
        

    command = input("Enter your command: ").strip()
    command_head = command.split(" ", maxsplit=1)[0]

    #  add command
    if command_head == "add":
        try:
            todo = command.split(" ", maxsplit=1)[1]
            todos.append(todo)
        except:
            error = "INVALID COMMAND."
    # rem command
    elif command_head == "rem":
        
        try:
            todo_number = int(command.split(" ", maxsplit=1)[1])
            #  check todo_number validation:
            if todo_number > len(todos):
                error = "TODO'S NUMBER OUT OF INDEX."
            elif todo_number < 1:
                error = "PLEASE ENTER A POSITIVE NUMBER."
            else:
                todos.pop(todo_number - 1)
        except:
            error = "INVALID COMMAND."
    #  non add/rem command
    else:
        error = "INVALID COMMAND."
        
    
    #  Save data to todos.txt
    
    #  Clear the file
    f = open("todos.txt", "w")
    f.close()
    #  Write todos in te file
    with open("todos.txt", "a") as f:
        for index, todo in enumerate(todos):
            if index != len(todos)-1:
                f.write(todo + "\n")
            else:
                f.write(todo)
            
