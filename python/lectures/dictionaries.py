# person = {
#     "fname" : "josh",
#     "lname" : "personson",
#     "age" : 32,
#     "age" : 4
# }

# print(person["fname"])

# person["fav_color"] = "blue"
# person["age"] += 1

# first_name = person["fname"]

# print(person["fav_color"])

# print(person.get("address", "No address found."))
# print(person.get("address", False))


# print(person.keys())
# print(person.value())
# print(person.items())

credentials = [{
    "username" : "mouse",
    "password" : "mice123"
}, {
    "username" : "cat",
    "password" : "tom123"    
}
]

username = input("Enter your username: ")
password = input("Enter your password: ")

for user in credentials:
    if user["username"] == username and user["password"] == password:
        print("Logged in successfully")
        break
else:
    print("Invalid username or password")