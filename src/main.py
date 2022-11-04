# main python file
import requests, json, riotapi, data, time

UPDATE = False
MATCHES_TO_UPDATE = 3

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
                data.update_match(match, riotapi.get_match(match))

    print('Total games:', len(data.read('data.json')))

    # get all matches for each player
    for player in players:
        kills = 0
        assists = 0
        deaths = 0
        totalGames = 0
        for match in data.get_matches(player):
            totalGames += 1
            for summoner in match['info']['participants']:
                if summoner['summonerName'] == player:
                    kills += summoner['kills']
                    assists += summoner['assists']
                    deaths += summoner['deaths']
        
        print(player + ' has ' + str(totalGames) + ' games\tKDA: ' + str((kills + assists) / deaths)[:4], 'Kills: ' + str(kills), 'Assists: ' + str(assists), 'Deaths: ' + str(deaths))
