# filenames = ["1.doc", "1.report", "1.presentation"]
# # transforming the strings
#
# filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
# print(filenames)


# new = []
#
# for i in [1, 2, 3]:
#     new.append(i + 10)
#
# print(new)


# old = [1, 2, 3]
# new = [i + 10 for i in old]
# print(new)

# new = [i for i in ['a', 'b', 'c']]
# print(new)


# names = ["john smith", "jay santi", "eva kuki"]
# names = [name.title() for name in names]
# print(names)


# usernames = ["john 1990", "alberta1970", "magnola2000"]
# chars = [len(item) for item in usernames]
# print(chars)


# user_entries = ['10', '19.1', '20']
# new_entries = [float(item) for item in user_entries]
# print(new_entries)


# user_entries = ['10', '19.1', '20']
# total = [float(item) for item in user_entries]
# print(sum(total))

numbers = [10.1, 12.3, 14.7]
numbers = [int(item) for item in numbers]
print(numbers)