while True:
    # get user info and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)        # todos is updated at this point

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:

        with open('todos.txt','r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]     #list comprehension

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}-{item}"
            print(row)
    elif 'edit' in user_action:
        number = user_action[5:]
        number = number - 1

        with open('todos.txt','r') as file:
            todos = file.readlines()

        new_todo = input("Enter new to do: ")
        todos[number] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    if 'complete' in user_action:
        number = int(input("Number of the todo to complete: "))

        with open('todos.txt','r') as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(number - 1)

        with open('todos.txt', 'w') as file:
             file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)

    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid")


print("bye")

