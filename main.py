# file = open("myfile.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("myfile.txt") as file:
    contents = file.read()
    print(contents)