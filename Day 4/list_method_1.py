# lekhna baaki xa hai GitHub bata

def get_second_element(x):
    return x[1]

a = [(3,0), (4,1), (12,10), (1,12)]
a.sort(key=get_second_element)
print(a) #[(3,0), (4,1), (12,10), (1,12)]


data =[(1,2,12), (3,1,14), (1,1), (5,2,0)]

#sort the above list based on last item of the each tuple

def get_last_element(x):
    return x[-1]

data.sort(key=get_last_element)
print(data)

data.sort(key=get_last_element,reverse=True)
print(data) #[(3, 1, 14), (1, 2, 12), (1, 1), (5, 2, 0)]

#reverse() ultyaune kaam matra order lai not descending




