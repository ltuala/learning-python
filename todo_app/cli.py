from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")

while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()
    
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for idx, todo in enumerate(todos):
            print(f"{idx+1}-{todo.strip('\n')}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            idx = number - 1

            todos = get_todos()       

            new_todo = input("Enter new todo: ")
            todos[idx] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print('Your command is not valid.')
            continue    

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            idx = number - 1
            todo_to_remove = todos[idx].strip('\n')

            todos = get_todos()      
            todos.pop(idx)

            write_todos(todos)
            
            message = f"Todo '{todo_to_remove}' was removed from the list"
            print(message)
        except IndexError:
            print('There is no item with that number.')
            continue
        
    elif user_action.startswith('exit'):
        break

    else:
        print("You entered an unknown command.")

print("Bye!")