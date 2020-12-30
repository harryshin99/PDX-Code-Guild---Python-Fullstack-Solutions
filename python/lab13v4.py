m_output = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
}

def convert_to_input(user_input, user_dist):
    for unit in m_output:
        if user_input == unit:
            converted_value = user_dist * m_output[unit]
    return converted_value
    
    # return [(user_dist * m_output[unit]) for unit in m_output if user_input == unit] # This returns a list. Could return index[0], but recommended for use for this situation.

def convert_to_output(converted_value, user_output):
    converted_value = convert_to_input(user_input, user_dist)

    for unit in m_output:
        if user_output == unit:
            converted_value = converted_value / m_output[unit]
    return converted_value

user_dist = input("What is the distance? ")
user_input = input("What are the input units? ")
user_output = input("What are the output units? ")

user_dist = float(user_dist)

converted_value = 0.0
converted_value = convert_to_output(converted_value, user_output)
converted_value = round(converted_value, 4)

print(f"{user_dist} {user_input} is {converted_value} {user_output}")