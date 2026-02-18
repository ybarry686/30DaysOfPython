"""
File Handling:
    To open a file: open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
        Modes:
            "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
            "a" - Append - Opens a file for appending, creates the file if it does not exist
            "w" - Write - Opens a file for writing, creates the file if it does not exist
            "x" - Create - Creates the specified file, returns an error if the file exists
            "t" - Text - Default value. Text mode
            "b" - Binary - Binary mode (e.g. images)
        
        Opening Files for Reading:
            read(): read the whole text as string. If we want to limit the number of characters we want to read, 
                    we can limit it by passing int value to the read(number) method.
            readlines(): reads all the text line by line and returns a list of the lines
                        Syntax: f.readlines()
            splitlines(): another way to read lines; syntax: f.read().splitlines()
            with open() as f: Closes files by itself, industry standard
                            
        Opening Files for Writing and Updating:
            Modes: 
                "a" - append - will append to the end of the file, if the file does not it creates a new file.            
                "w" - write - will overwrite any existing content, if the file does not exist it creates.

        Deleting Files:
            Must import the os module and use that to delete files; os.remove(file_path)
            If the file does not exist, the remove method will raise an error, so it is good to use an if condition like this:
                If file exist: .... else: ...
        
        File Types:
            Files with txt Extension:
                A very common form of data
            Files with json Extension:
                JSON stands for Javascript Object Notation; a stringifies JavaScript object of Python dictionary.
                Changing JSON to Dictionary
                    import json
                    json_to_dict = json.loads(json_var)
                Changing Dictionary to JSON
                    import json
                    dict_to_json = json.dumps(dict_var, indent=n) # indent can be 2, 4, 8, beautifies the json
                Saving as JSON File
                    import json
                    with open(...) as f: json.dump(dict_name, f, ensure_ascii, indent=n)
            Files with CSV Extension:
                CSV stands for comma separated values, stores tabular data, such as spreadsheets or databases
                Must import csv       
            Files with xlsx Extention
                To read excel files you must intall the xlrd package
                import xlrd
                excel_book = xlrd.open_workbook('sample.xls)
                print(excel_book.nsheets, excelbook.sheet_names) 
            Files with xml Extension
                Another structured data format that looks like HTML but tags are not predefined
                First line in an XML declaration
                Example Code:
                    import xml.etree.ElementTree as ET
                    tree = ET.parse('./files/xml_example.xml')
                    root = tree.getroot()
                    print('Root tag:', root.tag)
                    print('Attribute:', root.attrib)
                    for child in root:
                        print('field: ', child.tag)            
"""

import json
import re
import csv 
from collections import Counter
from Data.stop_words import stop_words

def main():
    read_files('./Data/obama_speech.txt', "Obama")    
    read_files('./Data/michelle_obama_speech.txt', "Michelle")    
    read_files('./Data/donald_speech.txt', "Donald")    
    read_files('./Data/melina_trump_speech.txt', "Melina")
    
    print(most_spoken_langs('./Data/countries_data.json', 10))   
    print(most_populated('./Data/countries_data.json', 10))
    print(find_all_emails('./Data/email_exchanges_big.txt'))
    print(find_most_common_words("I love python so much! The language is the best at the things it does, which is why I love it", 10))
    
    print(find_most_frequent_words('./Data/obama_speech.txt', 10))
    print(find_most_frequent_words('./Data/donald_speech.txt', 10))
    print(find_most_frequent_words('./Data/melina_trump_speech.txt', 10))
    print(find_most_frequent_words('./Data/michelle_obama_speech.txt', 10))
    print(find_most_frequent_words('./Data/romeo_and_juliet.txt', 10))
    
    print(hacker_news('./Data/hacker_news.csv', include="python"))
    print(hacker_news('./Data/hacker_news.csv', include="JavaScript"))
    print(hacker_news('./Data/hacker_news.csv', include="Java", exclude="JavaScript"))

def read_files(filename, name):
    with open(filename) as f:
        words = f.read()
        lines = words.splitlines()

        word_count = len(words)
        line_count = len(lines)
    
    print(f'Number of words in {name}\'s speech: {word_count}')
    print(f'Number of lines in {name}\'s speech: {line_count}') 
    print("-----")

def most_spoken_langs(filename, count):
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)
    
    languages = []
    
    for country in countries: 
        languages.append(country['languages'])
    
    language_counts = Counter([language for group in languages for language in group])
    
    return language_counts.most_common(count)

def most_populated(filename, count):
    with open(filename, 'r', encoding='utf-8') as f:
          countries = json.load(f)
    
    country_populations = [{'country': country['name'], 'population': country['population']} for country in countries]  
    
    country_populations.sort(key=lambda c: c['population'], reverse=True)
    
    return country_populations[0:count]

def find_all_emails(filename):
    with open(filename, encoding='utf-8') as f:
        txt = f.read()
    
    regex_pattern = r'[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]{2,}' # Email pattern

    emails = re.findall(regex_pattern, txt)
    
    return emails

def find_most_common_words(sentence, count):    
    return Counter(sentence.split(' ')).most_common(count)

def find_most_frequent_words(filename, count):
    with open(filename, encoding='utf-8') as f:
        txt = f.read()
    
    words = txt.split(' ')
    
    return Counter(words).most_common(count)

def hacker_news(filename, include, exclude=None):
    count = 0

    if isinstance(include, str):
        include = [include.lower()]
    if exclude != None and isinstance(exclude, str):
        exclude = [exclude.lower()]

    with open(filename) as f:
        reader = csv.reader(f)
         
        for row in reader:
            row_txt = " ".join(row).lower()
            
            if any(word in row_txt for word in include):
                if not exclude or not any(word in row_txt for word in exclude):
                    count += 1    
    return count

class CheckSimilarity:
    
    def __init__(self, txt1, txt2):
        self.txt1 = txt1
        self.txt2 = txt2

    def clean_text(self):
        with open(self.txt1, encoding='utf-8') as f1, open(self.txt2, encoding='utf-8') as f2:
            data1 = f1.read()
            data2 = f2.read() 
        
        regex_pattern = r'[A-Za-z]+'

        new_text1, new_text2 = re.findall(regex_pattern, data1), re.findall(regex_pattern, data2)

        return new_text1, new_text2

    def remove_support_words(self):
        clean1, clean2 = self.clean_text()

        for word in clean1[:]:
            if word.lower() in stop_words:
                clean1.remove(word)   

        for word in clean2[:]:
            if word.lower() in stop_words:
                clean2.remove(word)          

        return clean1, clean2

    def check_text_similarity(self):
        clean1, clean2 = self.remove_support_words()

        new_clean1 = set(clean1)
        new_clean2 = set(clean2)
        matching_words = new_clean1 & new_clean2

        percent_overlap = (len(matching_words) / (len(new_clean1) | len(new_clean2))) * 100

        print(f'There was a total of {len(matching_words)} matching words between both text!')
        print(f'This results in a {percent_overlap}% overlap')
        
        return matching_words

checker = CheckSimilarity('./Data/obama_speech.txt', './Data/donald_speech.txt')
print(checker.check_text_similarity())

main()