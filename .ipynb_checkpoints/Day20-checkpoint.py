
"""
Machine Learning Packages:
    Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.
    Pandas: is a data analysis, data science and a machine learning library in Python that provides data structures of high-level and a wide variety of tools for analysis.
    SciPy: SciPy is a machine learning library for application developers and engineers. 
        SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
    Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
    TensorFlow: is a machine learning library built by Google.
    Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks.
        Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.
"""
import numpy as np
import webbrowser
import requests
import statistics
from collections import Counter

# print(np.version.version)

# lst = [1,2,3,4,5]
# np_arr = np.array(lst)
# np_arr = np_arr * 2
# np_arr = np_arr + 2


# url_lists = [
#     'http://www.python.org',
#     'https://www.linkedin.com/in/asabeneh/',
#     'https://github.com/Asabeneh',
#     'https://twitter.com/Asabeneh',
# ]

# for url in url_lists:
#     webbrowser.open_new_tab(url)

def cats_api(cats_url, dict_key, dict_vals=None):
    cats_response = requests.get(cats_url)
    cats_json = cats_response.json()

    if dict_vals:
        cat_data = [cat[dict_key][dict_vals] for cat in cats_json]
    else:
        cat_data = [cat[dict_key] for cat in cats_json]
    
    pairs = [(int(lower), int(upper)) for lower, upper in (item.split('-') for item in cat_data)]
    
    flattened_data = [num for pair in pairs for num in pair]

    return {
        dict_key: {
            "min": min(a for a, b in pairs),
            "max": max(b for a, b in pairs),
            "mean": statistics.mean(flattened_data),
            "median": statistics.median(flattened_data),
            "std_dev": statistics.stdev(flattened_data),
        }
    }

print(cats_api('https://api.thecatapi.com/v1/breeds', 'weight', 'metric'), cats_api('https://api.thecatapi.com/v1/breeds', 'life_span'))

"""
Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
the min, max, mean, median, standard deviation of cats' weight in metric units.
the min, max, mean, median, standard deviation of cats' lifespan in years.
Create a frequency table of country and breed of cats
"""