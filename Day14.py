from functools import reduce
"""
Higher Order Functions
    - Python Closures:
        - Functions withinw
        - A design pattern in python that allows a user to add new fucntionality to an existing
          object without modifying it's structure
        - Decorators are typically called before the definition of a function you want to decorate
        - Decorators are interpreted in a top-down order during runtime but execute bottom-up order during definition 
    - Built-in Higher Order Functions:
        - map() function: takes in a function, and iterable (ex:list) as parameters 
            - Returns iterable after changes from input function are applie to it
        - filter() function: takes in a fucntion, and iterable (ex:list) as parameters
            - Returns true or false for each element in iterable, all true values are returned as iterable
        - reduce() function: defined in the functools module, should be imported from module; 
            - takes in a function, and iterable (ex:list) as parameters 
            - Returns a single value
"""
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random = ['Hello', 'World', 2, 10, 40, True, False]

def raise_power(x):
    return x ** 2

def uppercase_countries(country):
    return country.upper()

def uppercase_names(names):
    return names.upper()

def countries_without_land(country):
    land = 'land'
    if land in country:
        return False
    return True

def sixLetter_countries(country):
    if len(country) == 6:
        return False
    return True

def long_countries(country):
    if len(country) >= 6:
        return False
    return True

def start_withE_countries(country):
    if country[0] == 'E':
        return False
    return True

def sum_numbers(numbers, x):
    res = 0
    for num in x:
        res += num
    return res

def large_values(x):
    if x >= 25:
        return False
    return True

def get_string_lists(arr):
    res = []
    for i, item in enumerate(arr):
        arr[i] = str(item)
        res.append(str(item))
    
    return arr, res

def reduce_sum_numbers(x, y): 
    return x + y

def north_african_only(func, countries):
    def wrapper(countries):
        pass
    return wrapper

print(list(map(raise_power, numbers)))
print(list(map(uppercase_countries, countries)))
print(list(map(uppercase_names, names)))

print(list(filter(countries_without_land, countries)))
print(list(filter(sixLetter_countries, countries)))
print(list(filter(long_countries, countries)))
print(list(filter(start_withE_countries, countries)))

print(get_string_lists(random))
print(reduce(reduce_sum_numbers, numbers))
print(reduce())




"""
Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
"""
