todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = []
            # for todo in todos:
            #     new_todo = todo.strip('\n')
            #     new_todos.append(new_todo)

            # new_todos = [item.strip('\n') for item in todos]

            # for idx, todo in enumerate(new_todos):
            for idx, todo in enumerate(todos):
                print(f"{idx+1}-{todo.strip('\n')}")

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            idx = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()        

            new_todo = input("Enter new todo: ")
            todos[idx] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                todos = file.writelines()    

        case 'complete':
            number = int(input("Number of the todo to complete: "))
            idx = number - 1
            todo_to_remove = todos[idx].strip('\n')

            with open('todos.txt', 'r') as file:
                todos = file.readlines()        
            todos.pop(idx)

            with open('todos.txt', 'w') as file:
                todos = file.writelines()
            
            message = f"Todo '{todo_to_remove}' was removed from the list"
            print(message)
        case 'exit':
            break

        case _:
            print("You entered an unknown command.")

print("Bye!")