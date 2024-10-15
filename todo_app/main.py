user_prompt = "Enter a todo: "
todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo)

    add_more = input("Continue? [Y/N] ")
    if add_more.strip().lower() != "y":
        break
    continue

print(todos)