# store even numbers in a a list in range 0-50


    
data =[1,2,1,3,4,5,6,2,1]

result = []

for i in data:
    if data.count(i)>1 and i not in result: 
        result.append(i)


print(result)