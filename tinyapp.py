import json

jsonPath = './data/content.json'

def readJson(path):
    '''Read JSON'''
    with open(path, 'r') as file:
        info = json.load(file)

    print(info)

if __name__ == '__main__':
    readJson(jsonPath)
