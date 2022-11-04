# updates the file containing player match history
import json

def read(fileName):
    return json.load(open(fileName, 'r'))

def write(fileName: str, data):
    json.dump(data, open(fileName, 'w'))

def update_match(match, data):
    jsonData = read('data.json')
    if not jsonData.get(match):
        jsonData[match] = data
        write('data.json', jsonData)