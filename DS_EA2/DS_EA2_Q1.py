# Empfehlung: anaconda verwenden als Paketquelle

import random
import sys
import time
import numpy as np

values=[
    [23, 104, 5, 190, 8, 7, -3],
    [],
    ]
def addRandomValues(cnt):
    values.append([random.randint(-sys.maxsize - 1, sys.maxsize) for _ in range(cnt)])
    
def timingTest(fkt):
    for value in values:
        if value is None:
            raise ValueError("value is None")
        if any(not isinstance(item, (int, float)) for item in value):
            raise ValueError("value contains non-numeric values")
        timeFunction(fkt, value)
            
def timeFunction(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    title = f"with {len(*args)} values " if isinstance(*args, list) else ""
    print(f"{func.__name__} {title} took {str(end - start)} seconds")

def getSortedIndexesNoNumpy(unsorted):
    return map_back(sort_indexed(map_indexes(unsorted)))

def getSortedIndexesUsingNumpy(unsorted):
    return np.argsort(unsorted)

def map_indexes_manual(lst):
    result = []
    idx = 0            
    for item in lst:
        result.append((item, idx))    
        idx += 1
    return result    
def map_indexes(list):
    return [(list[i], i) for i in range(len(list))]

def map_indexes_enumerate(lst):
    return [(num, index) for index, num in enumerate(lst)]    
 
def sort_indexed(lst):
    return sorted(lst, key=lambda x: x[0])    

def map_back(list):
    return [item[1] for item in list]
        
timeFunction(addRandomValues, 1000000)

timingTest(getSortedIndexesNoNumpy)
timingTest(getSortedIndexesUsingNumpy)

print(getSortedIndexesNoNumpy(values[0]))
print(getSortedIndexesUsingNumpy(values[0]))
# the values are the same, though numpy returns an array, not a python list.

# addRandomValues  took 3.760301351547241 seconds
# getSortedIndexesNoNumpy with 7 values  took 0.0 seconds
# getSortedIndexesNoNumpy with 0 values  took 0.0 seconds
# getSortedIndexesNoNumpy with 1000000 values  took 3.8775322437286377 seconds
# getSortedIndexesUsingNumpy with 7 values  took 0.0 seconds
# getSortedIndexesUsingNumpy with 0 values  took 0.0 seconds
# getSortedIndexesUsingNumpy with 1000000 values  took 0.1756744384765625 seconds

print("numpy is wayyy faster.")