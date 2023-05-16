user_message = "Enter a todo: "

todos = []

while True:
    todo = input(user_message)
    print(todo.title())
    todos.append(todo)

