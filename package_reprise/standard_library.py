####--------------------------------STANDARD LIBRARY-----------------------------------####

##--------------ALL IMPORTS-----------##
import array
import math
import random
import os
import shutil
import json
import csv
from datetime import datetime, timedelta
import re

## ARRAY
arr = array.array('i', [1, 2, 3, 4])
print(arr)


## MATH
print(math.sqrt(256))
print(math.pi)


## RANDOM
print(random.randint(1, 10))
print(random.choice(['apple', 'banana', 'cherry', 'pineapple']))


## FILE - DIRECTORY ACCESS
print(os.getcwd())

## MAKE DIRECTORY
os.mkdir(('test_dir'))

## HIGH LEVEL OPERATIONS ON FILES AND COLLECTION OF FILES
shutil.copyfile('source.txt', 'destination.txt')

## DATA SERIALIZATION
data = {'name': 'Jeffrey', 'Occupation': 'Solver'}
json_str = json.dumps(data)
print(json_str)
print(type(json_str))


parsed_data = json.loads(json_str)
print(parsed_data)
print(type(parsed_data))


## csv
with open('newdata.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age'])
    writer.writerow(['Gauss', 1729])

with open('newdata.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


## DATETIME
now = datetime.now()
print(now)

yesterday = now - timedelta(days=1)
print(yesterday)

print(yesterday)

## REGULAR EXPRESSION
pattern = r'\d+'
text = 'It took 2 to get 3. There are 2 unique prime numbers in this text'
match = re.search(pattern, text)
print(match.group())