# updates the file containing player match history
import json
FILE_NAME = 'data.json'

def read(fileName):
    return json.load(open(fileName, 'r'))

def write(fileName: str, data):
    json.dump(data, open(fileName, 'w'))

def update_match(match, data):
    jsonData = read(FILE_NAME)
    if not jsonData.get(match):
        print('Adding match: ' + match)
        jsonData[match] = data
        write(FILE_NAME, jsonData)

def get_match(match):
    return read(FILE_NAME)[match]

#read match data
def get_matches(player):
    matches = []
    for _, match in read(FILE_NAME).items():
        for summoner in match['info']['participants']:
            if summoner['summonerName'] == player:
                matches.append(match)
                break
    
    return matches