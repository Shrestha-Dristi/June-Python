


# a = 0
# while a <= 10:
#     if a == 5:
#         a += 1
#         continue
#     print(a)
#     a += 1


# Paxi ko kura
# 1. Date/time
def combine_dictionaries(dict1, dict2):
    # # Create a new dictionary to store the combined results
    # combined_dict = {}

    # # Iterate through the first dictionary and add its key-value pairs to the combined dictionary
    # for key, value in dict1.items():
    #     combined_dict[key] = value

    combined_dict = dict1.copy()

    # Iterate through the second dictionary
    for key, value in dict2.items():
        if key in combined_dict:
            # If the key exists in the combined dictionary, add the values
            combined_dict[key] += value
        else:
            # If the key does not exist, add the key-value pair to the combined dictionary
            combined_dict[key] = value

    return combined_dict

# Example dictionaries
dict2 = {'a': 100, 'b': 200, 'c': 300}
dict1 = {'a': 300, 'b': 200, 'd': 400}

# Combine the dictionaries
result = combine_dictionaries(dict1, dict2)

# Print the combined dictionary
print("Combined Dictionary:", result)

print(dict1)
print(dict2)
