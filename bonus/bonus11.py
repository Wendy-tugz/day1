# def get_average():
#     with open("files2/data.txt", 'r') as file:
#         data = file.readlines()
#
#     values = data[1:]
#     values = [float(i) for i in values]
#
#     average_local = sum(values) / len(values)
#     return average_local
#
#
# average = get_average()
# print(average)


# def get_average():
#     print("Hi")
#     x = "hello"
#
#
# print(get_average())


# def get_maxvalue():
#     grades = [9.6, 9.2, 9.7]
#
#     maxvalue = max(grades)
#     minvalue = min(grades)
#     message = f"Max: {maxvalue}, Min: {minvalue}"
#     return message
#
#
# print(get_maxvalue())

def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius = get_maximum()

fahrenheit = celsius * 1.8 + 32
print(fahrenheit)


