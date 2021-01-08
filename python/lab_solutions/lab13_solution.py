
conversion = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}

def validate_unit(message):
    while True:
        unit = input(message)
        if unit not in conversion:
            print(f"Invalid unit. Choose one of the following: {' '.join(list(conversion.keys()))}")
            continue
        else:
            return unit

distance = input("Enter distance to convert:")

distance = float(distance)

in_unit = validate_unit("Enter unit to convert from: ")
out_unit = validate_unit("Enter unit to convert to: ")

num_meters = distance * conversion[in_unit]

result = num_meters / conversion[out_unit]

print(f"{distance} {in_unit} is {result} {out_unit}")