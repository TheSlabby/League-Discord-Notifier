# main python file
import requests, json, riotapi, data

players = ['TheSlabby', 'TheStair']

if __name__ == '__main__':
    # create data.json if it doesn't exist
    try:
        data.read('data.json')
    except:
        data.write('data.json', {})

    for player in players:
        id = riotapi.get_id(player)
        matches = riotapi.get_matches(id, 3)
        for match in matches:
            data.update_match(match, riotapi.get_match(match))