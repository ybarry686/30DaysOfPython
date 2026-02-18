"""
List Comprehensions:
    - Considerably faster than using loops to achieve the same result, do to the bytecode interpreter in C

Lambda Functions:
    - A small anonymous function without a name. It can take any number of arguments, but can only have one expression.
    - Useful when trying to write an anonymous function inside another function
    - Syntax:
        - name_of_function = lambda param1, param2, paramN: param1 {do something} param2 {do something} paramN
"""

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_nums = [i for i in numbers if i <= 0]
print(neg_nums)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
combined_list = [num for sub_list in list_of_lists for num in sub_list]
print(combined_list)


list_of_tups = [tuple([i] + [i ** j for j in range(0, 6)]) for i in range(11)]
print(list_of_tups)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_abrev = [[country[0].upper(), country[0][:3].upper(), country[1].upper()] for sub_list in countries for country in sub_list]
print(countries_abrev)

dict_of_countries = [{'country': country.upper(), 'city': city.upper()} for sub_list in countries for (country, city) in sub_list]
print(dict_of_countries)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [(first + " " + last) for sub_list in names for (first, last) in sub_list]
print(full_names)

"""
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

['country\': ' country,'city\': 'city]
"""