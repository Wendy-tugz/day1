# contents = ["All the carrots are to be sliced "
#             "longitudinally",
#             "The carrots were reportedly sliced",
#             "The slicing process was well presented"]
#
# filenames = ["doc.txt", "report.txt", "presentation.txt"]
#
# for content, filename in zip(contents, filenames):
#     file = open(f"../files/{filename}", 'w')
#     file.write(content)


# words = ["The true meaning of obscurity "
#         "lies underneath the most delicate structures of viscosity. "
#         "The idea of changing that balance is obscure by itself."]
#
# filenames = ['essay.txt']
#
# for word, filename in zip(words, filenames):
#     file = open(f"../files/{filename}", 'r')
#     words = file.read()
#     file.close()
#
#
#     print(len(words))


# member = input("Add a new member: ")
# file = open(f"../files/members.txt", 'r')
# existing_members = file.readlines()
# file.close()
#
# existing_members.append(member + "\n")
#
# file = open(f"../files/members.txt", 'w')
# existing_members = file.writelines(existing_members)
# file.close()


# contents = ["Hello ",
#             "Hello",
#             "Hello"]
#
# filenames = ["h1.txt", "h2.txt", "h3.txt"]
#
# for content, filename in zip(contents, filenames):
#     file = open(f"../files/{filename}", 'w')
#     file.write(content)
#     file.close()


# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for filename in filenames:
#     file = open(filename, 'w')
#     file.write("Hello")
#     file.close()


filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f"../files/{filename}", 'r')
    content = file.read()
    file.close()
    print(content)