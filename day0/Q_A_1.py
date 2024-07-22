
# Write a Python program to combine two dictionaries by adding values for common keys.
def combine_dicts(dict1,dict2):

    combined_dict = dict1.copy()

    for key, value in dict2.items():

        if key in combined_dict:
            
            combined_dict[key] += value
        
        else:

            combined_dict[key] = value

    return combined_dict

dict2 = {'a': 100, 'b': 200, 'c': 300}
dict1 = {'a': 300, 'b': 200, 'd': 400}

result = combine_dicts(dict1,dict2)

print(result)
# output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}