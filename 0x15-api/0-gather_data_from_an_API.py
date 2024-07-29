#!/usr/bin/python3
from ast import literal_eval
import urllib.request
import sys

if __name__ == "__main__":
    # Fetch data from url
    uid = sys.argv
    req = urllib.request.Request('https://jsonplaceholder.typicode.' + 
                        'com/todos/' + f'{int(uid[1])}')
    with urllib.request.urlopen(req) as response:
        fetched_data = response.read()
        i = 0
        for chrs in fetched_data:
            if chrs == '/n':
                fetched_data[i] = 'o'
            i += 1
        fetched_data = fetched_data.decode('utf-8')
    
    print(type(fetched_data))
    print(fetched_data)
