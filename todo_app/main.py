todos = []

while True:
    user_action = input("Type add, show, or exit: ").strip()
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for todo in todos:
                print(todo)
        case 'exit':
            break
        case _:
            print("You entered an unknown command.")

print("Bye!")