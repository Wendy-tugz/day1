# try:
#     width = float(input("Enter rectangle width: "))
#     length = float(input("Enter rectangle length: "))
#     if width == length:
#         exit("That looks like a square.")
#
#     area = width * length
#     print(area)
# except ValueError:
#     print("Please enter a number.")

# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#     if total_value == 0:
#         exit("Your total value can not be zero.")
#
#     percentage = (value / total_value) * 100
#     print(f"That is {percentage}%")
# except ValueError:
#     print("You need to enter a number. Run the program again.")

# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#
#     percentage = (value / total_value) * 100
#     print(f"That is {percentage}%")
# except ValueError:
#     print("You need to enter a number. Run the program again.")
# except ZeroDivisionError:
#     print("Your total value can not be zero.")

try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print(f"{name} is not on the list.")

