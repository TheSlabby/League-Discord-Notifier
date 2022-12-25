# main python file
import requests, json, sys
import riotapi, discordhook, mongod # custom libraries

UPDATE = True
MATCHES_TO_UPDATE = 2
HOOK_URL = open('.key', 'r').readlines()[1].strip()

players = open('players.config', 'r').read().splitlines()

if __name__ == '__main__':
    conn = mongod.get_connection()
    if not conn: sys.exit()
    # create data.json if it doesn't exist
    # try:
    #     data.read('data.json')
    # except:
    #     data.write('data.json', {})

    # check last 3 matches for each player to see if there are any new matches to add
    if UPDATE:
        try:
            for player in players:
                print('Checking matches for ' + player)
                id = riotapi.get_id(player)
                matches = riotapi.get_matches(id, MATCHES_TO_UPDATE)
                for match in matches:
                    matchData = riotapi.get_match(match)
                    if not mongod.add_match(matchData):
                        print('Match already exists')

                    # if data.update_match(match, matchData):
                    #     # find all players in match
                    #     for player in players:
                    #         playerData = data.get_player_data(matchData, player)
                    #         if playerData:
                    #             embed = discordhook.match_embed(matchData, player)
                    #             #discordhook.send_hook('', embed) #comment if u dont want to spam ur webhook
        except KeyboardInterrupt:
            print('cancelled - ctrl+c\n\n')

    # print('Total games:', len(data.read('data.json')))

    # data.fix_data() # sometimes data gets corrupted :(

    # get all matches for each player
    # for player in players:
    #     kills = 0
    #     assists = 0
    #     deaths = 0
    #     totalGames = 0
    #     for match in data.get_matches(player):
    #         totalGames += 1
    #         playerData = data.get_player_data(match, player)
    #         kills += playerData['kills']
    #         assists += playerData['assists']
    #         deaths += playerData['deaths']
        
    #     print(player + ' has ' + str(totalGames) + ' games\nKDA: ' + str((kills + assists) / deaths)[:4], 'Kills: ' + str(kills), 'Assists: ' + str(assists), 'Deaths: ' + str(deaths) + '\n')
