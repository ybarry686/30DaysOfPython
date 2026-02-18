"""
Regular Expressions (RegEx):
---> A special text string to help you find patterns in data. A RegEx can be used to check if some pattern exists in
     a different data type.
---> Must be imported using 'import re'
---> To find a pattern we use different set of re character sets that allows to search for a match in a string.
-----> re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
--------> re.match(substring, string, re.I) # substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
-----> re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
-----> re.findall: Returns a list containing all matches
-----> re.split: Takes a string, splits it at the match points, returns a list
-----> re.sub: Replaces one or many matches within a string
-----> re.I: This parameter ignores cases for letters
--------> Other Alternatives: matches = re.findall('Python|python', txt), matches = re.findall('[Pp]ython', txt) 
---> regex patterns: 
-----> Multiple things: r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
-----> Escape Chars: regex_pattern = r'\d'  # d is a special character which means digits
-----> One or More: regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
-----> Period: regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
-----> Zero or More: regex_pattern = r'[a].*'  # . any character, * any character zero or more times 
-----> Cart (Starts With): regex_pattern = r'^This'  # ^ means starts with
-----> regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
"""

import re
from collections import Counter

def main():
    print(find_word_counts('''I love teaching. If you do not love teaching what else can you love. 
                           I love Python if you do not love something which can give you all the capabilities to 
                           develop an application what else can you love.'''))
    
    print(distance_between_particles('''The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 
          0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the 
          distance between the two furthest particles.'''))
    
    print(is_valid_variable('first_name'), # True
          is_valid_variable('first-name'), # False
          is_valid_variable('1first_name'), # False
          is_valid_variable('firstname')) # True)
    
    print(clean_text('''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. 
            ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''))
    
    print(find_word_counts(clean_text('''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. 
            ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?''')))

def find_word_counts(txt):
    words = re.findall(r'\b\w+\b', txt)
    freq = Counter(words)
    result = sorted([(count, word) for word, count in freq.items()], reverse=True)

    return result

def distance_between_particles(txt):
    regex_pattern = r'-?\d+'
    match = re.findall(regex_pattern, txt)
    
    for i, val in enumerate(match):
        match[i] = int(val)

    match.sort()
    
    return match[-1] - match[0]

def is_valid_variable(txt):
    regex_pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
    return bool(re.match(regex_pattern, txt))

def clean_text(txt):
    regex_pattern = r'[@!#$%^&;,.?]+'
    cleaned_string = re.sub(regex_pattern, '', txt)
    
    return cleaned_string

main()

"""
Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. 
            ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

print(clean_text(sentence));
I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs 
Does this motivate you to be a teacher
print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]

"""