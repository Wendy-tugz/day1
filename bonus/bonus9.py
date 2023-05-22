# password = input("Enter New Password: ")
#
# result = {}
#
# if len(password) >= 8:
#     result["length"] = True
# else:
#     result["length"] = False
#
# digit = False
#
# for i in password:
#     if i.isdigit():
#         digit = True
#
# result["digits"] = digit
#
# uppercase = False
# for i in password:
#     if i.isupper():
#         uppercase = True
#
# result["upper-case"] = uppercase
#
# print(result)
#
# if all(result.values()):
#     print("Strong password.")
# else:
#     print("Weak password.")



# password = input("Enter New Password: ")
#
# result = []
#
# if len(password) > 7:
#     print("Great password there!")
#
# if len(password) == 7:
#     print("Password is OK, but not too strong")
# else:
#     print("Your password is weak")



# ids = ["XF345_89", "XER76849", "XA454_55"]
#
# x = 0
#
# for id in ids:
#     if '_' in id:
#         x = x + 1
# print(x)

# ids = ["XF345_89", "XER76849", "XA454_55"]
#
# x = 0
#
# for id in ids:
#     if '_' in id:
#         x = x + 1
# print(x)


length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = (length + width) * 2
area = length * width

print("Perimeter is", perimeter)
print("Area is", area)

if perimeter < 14 and area < 8:
    print("OK")
else:
    print("NOT OK")
