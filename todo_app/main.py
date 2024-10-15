todos = []

while True:
    user_action = input("Type add, show, edit, or exit: ").strip()
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for todo in todos:
                print(todo)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            idx = number - 1
            new_todo = input("Enter new todo: ")
            todos[idx] = new_todo
        case 'exit':
            break
        case _:
            print("You entered an unknown command.")

print("Bye!")