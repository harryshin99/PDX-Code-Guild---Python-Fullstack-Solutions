# def has_key(d, key):
    # if key in d:
    #     return True
    # else:
    #     return False

    # for k in d:
    #     if k == key:
    #         return True
    # return False

    # return key in d

# print(has_key({'a': 1, 'b': 2}, 'a')) # True
# print(has_key({'a': 1, 'b': 2}, 'c')) # False


# def is_empty(d):
    # if len(d) == 0:
    #     return True
    # else:
    #     return False
    
    # return len(d) == 0

    # return not(len(d) != 0)

    # return not(d)

# print(is_empty({})) # True
# print(is_empty({'a': 1, 'b': 2})) # False


# def find_key(d, value):
#     for key in d:
#         if value == d[key]:
#             return key
#     return None

#     # result = [key for key in d if d[key] == value]
#     # return result[0] if result else None

#     # return [key for key in d if d[key] == value][0] if [key for key in d if d[key] == value] else None

# print(find_key({'a': 1, 'b': 2}, 1)) # a
# print(find_key({'a': 1, 'b': 2}, 3)) # None


# def reverse_dict(d):
#     # new_dict = {}
#     # for key, value in d.items():
#     #     new_dict[value] = key

#     # for key in d:
#     #     new_dict[d[key]] = key
    
#     # return new_dict

#     return {d[key]: key for key in d}

# print(reverse_dict({'a': 1, 'b': 2})) # {1: 'a', 2: 'b'}


# def merge(list1, list2):
#     # merged_dict = {}
#     # for index in range(len(list1)):
#     #     # merged_dict[list1[index]] = list2[index]

#     #     merged_dict.update({list1[index]: list2[index]})

#     # return merged_dict

#     return {list1[index]: list2[index] for index in range(len(list1))}

# print(merge(['a', 'b'], [1, 2])) # {'a': 1, 'b': 2}


def remove_less_than_10(d):
    new_dict = {}
    for d_index in d:
        if d[d_index] > 10:
            new_dict[d_index] = d[d_index]
    return new_dict

print(remove_less_than_10({'a': 5, 'b': 15, 'c': 12})) # {'b': 15, 'c': 12}