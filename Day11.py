
def get_user_data():
    name = input("Type your name: ")
    age = input("Type your age: ")

    if int(age) >= 50:
        print("you are old")
    elif int(age) >= 30:
        print("your middle aged")
    else:
        print("your young and youthful")

print(get_user_data())

"""
Importing Modules
- Sys Module: Provides functions and variables to manipulate different parts 
              of the python runtime environment.
    - sys.argv: returns a list of command line arguments passed to a python script
        - Item at index 0 is always the name of the script, at index one the argument
          passed from the command line
    - sys.exit()
    - sys.maxsize
    - sys.path
    - sys.version

- Stats Module: Provides functions for mathematical statistics of numeric data
    - mean
    - median
    - mode
    - stdev
"""




