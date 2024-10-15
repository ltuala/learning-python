todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            for idx, todo in enumerate(todos):
                print(f"{idx+1}-{todo}")
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            idx = number - 1
            new_todo = input("Enter new todo: ")
            todos[idx] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            idx = number - 1
            todos.pop(idx)
        case 'exit':
            break
        case _:
            print("You entered an unknown command.")

print("Bye!")