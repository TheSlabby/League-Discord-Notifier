# main python file
import requests, json, riotapi, data

UPDATE = True
MATCHES_TO_UPDATE = 3
HOOK_URL = open('.key', 'r').readlines()[1].strip()

players = [
    'TheSlabby', 'TheStair', 'hgihy', 'zyraonetrick', 'JonStory',
    'LaxusWho', 'faineant24', 'Zombieslasher5', 'JJKINGX', '4LT4R',
    'cvjwqnri', 'Shanerman101'
]

if __name__ == '__main__':
    # create data.json if it doesn't exist
    try:
        data.read('data.json')
    except:
        data.write('data.json', {})

    # check last 3 matches for each player to see if there are any new matches to add
    if UPDATE:
        for player in players:
            print('Checking matches for ' + player)
            id = riotapi.get_id(player)
            matches = riotapi.get_matches(id, MATCHES_TO_UPDATE)
            for match in matches:
                matchData = riotapi.get_match(match)
                if data.update_match(match, matchData):
                    playerData = data.get_player_data(matchData, player)
                    msg = '*' + player + ' just played a match:*\n'
                    msg += 'Champion: **' + playerData['championName'] + '**\n'
                    msg += 'KDA: **' + str(playerData['kills']) + '/' + str(playerData['deaths']) + '/' + str(playerData['assists']) + '**\n'
                    msg += 'Damage: **' + str(playerData['totalDamageDealtToChampions']) + '**\n'
                    msg += 'Gold: **' + str(playerData['goldEarned']) + '**\n'
                    msg += 'Result: **' + ('Victory' if playerData['win'] else 'Defeat') + '**\n'

                    # send webhook to discord >:)
                    obj = json.loads(json.dumps({'content': msg}))
                    requests.post(HOOK_URL, data=obj)
                    print(msg)

    print('Total games:', len(data.read('data.json')))

    # get all matches for each player
    for player in players:
        kills = 0
        assists = 0
        deaths = 0
        totalGames = 0
        for match in data.get_matches(player):
            totalGames += 1
            playerData = data.get_player_data(match, player)
            kills += playerData['kills']
            assists += playerData['assists']
            deaths += playerData['deaths']
        
        print(player + ' has ' + str(totalGames) + ' games\nKDA: ' + str((kills + assists) / deaths)[:4], 'Kills: ' + str(kills), 'Assists: ' + str(assists), 'Deaths: ' + str(deaths) + '\n')
