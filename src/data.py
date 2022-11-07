# updates the file containing player match history
import json
FILE_NAME = 'data.json'
BROADCAST = True #send message to webhook

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
        
        return True
    return False

def fix_data():
    jsonData = read(FILE_NAME)
    fixedData = jsonData.copy()
    for key, match in jsonData.items():
        if not match.get('info'):
            print('Found corrupted match:', key)
            del fixedData[key]
    
    write(FILE_NAME, fixedData)

def get_player_data(match, player):
    for summoner in match['info']['participants']:
        if summoner['summonerName'] == player:
            return summoner

def get_match(match):
    return read(FILE_NAME)[match]

# read match data
def get_matches(player):
    matches = []
    for _, match in read(FILE_NAME).items():
        if get_player_data(match, player):
            matches.append(match)
    
    return matches 