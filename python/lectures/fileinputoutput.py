

# file = open('stuff.txt')

# print(file.read())

# with open('./python/lectures/stuff.txt', 'r') as file:
#     print(file.read())
def length(elem):
    return len(elem)

while True:
    name = input("Enter a name: ")

    if name == 'done':
        break

    with open('names.txt', 'a') as file:
        file.write(name + '\n')

with open('names.txt', 'r') as file:
    contents = file.read()

names = contents.split('\n')
names.sort()

# longest_name = names[0]
# for name in names:
#     if len(name) > len(longest_name):
#         longest_name = name

names.sort(key=length)

# names.sort(key=lambda e: len(e))

print(names[-1])