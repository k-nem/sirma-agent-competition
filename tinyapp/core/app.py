import json
import os

# jsonPath = '../data/content.json'

jsonPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/content.json'))
global a
info = None

def readJson(path):
    '''Read JSON'''
    with open(path, 'r') as file:
        info = json.load(file)

    return info

if __name__ == '__main__':
    a = readJson(jsonPath)
    print(a)
