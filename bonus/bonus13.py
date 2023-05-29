# feet_inches = input("Enter feet and inches: ")
#
#
# def parse(feet_inches):
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#     return {"feet": feet, "inches": inches}
#
#
# def convert(feet, inches):
#     meters = feet * 0.3048 + inches * 0.0254
#     return meters
#
#
# parsed = parse(feet_inches)
#
# result = convert(parsed['feet'], parsed['inches'])
#
# print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")
#
# if result < 1:
#     print("Kid is too small.")
# else:
#     print("Kid can use the slide.")


# def get_age(year_of_birth, current_year=2023):
#     age = current_year - year_of_birth
#     return age
#
# birthyear = int(input("What is your year of birth? "))
# age = get_age(birthyear)
# print(age)
#
# if age > 120:
#     print("Oh men! You're old")

# def get_nr_items(user_input):
#     items = user_input.split(',')
#     return len(items)
#
#
# names = input("Enter names separated by commas (no spaces): ")
# nr_items = get_nr_items(names)
# print(nr_items)

def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)