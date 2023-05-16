user_message = "Enter a todo: "

todos = []


#while loop 1
while True:
    todo = input(user_message)
    #stores todos in a list
    todos.append(todo) #append is a method, which are attached to data types
    print(todos)
