""" 
Exception Handling:
--> Try: Run this code
--> Except: Execute this code if an exception is encountered
--> Else: Run this if there is no exception
--> Finally: Always run this code

Packing and Unpacking Arguments:
--> Unpacking:
---->* for tuples
----> ** for dicts
--> Packing:
----> If you don't know how many arguments will be passed into a python function use * for lists, and ** for dicts
------> Ex for lists: def unkwown_parameters_forLists(*args):
------> Ex for dicts: def unknown_parameters_forDicts(**kwargs)
"""
# Exception handling
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2025 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

# Unpacking
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  
# print(sum_of_five_nums(lst)), results in TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'

numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.

# Packing 
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))

# Spreading
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

# Zip
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)

"""
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. 
Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
"""
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia'] 
*nordic, es, ru = names
print(f'{nordic}, {es}, {ru}')
