'''
Problem 1: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

>>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
{'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
'''

def flatten_dict(dictionary):
    newdict =dict()
    for i in dictionary.keys():

        key = i
        value = dictionary[i]
       
        x = isinstance(value, dict)
        if (x == False):
            newdict[key]= value
            # print (newdict)
        else:
            for o in value:
                newvalue = value[o]
                newkey = key + "." + o
                newdict[newkey] = newvalue
    print(newdict)


        


    # for i in dictionary:
    #     print(i)
    #  x = isinstance(i, dict)
    #     print(x)


# 1
# False
# {'x': 2, 'y': 3}
# True
# 4
# False


flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})


'''
Problem 2: Write a function unflatten_dict to do reverse of flatten_dict.

>>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
{'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
'''



'''
Problem 3: Write a function treemap to map a function over nested list.

>>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
[1, 4, [9, 16, [25]]]
'''

