import data
import time, requests, json

players = open('players.config', 'r').read().splitlines()
HOOK_URL = open('.key', 'r').readlines()[1].strip()

if __name__ == '__main__':
    report = ''
    print('Getting report for players...')
    for player in players:
        totalGames, kills, deaths, assists, wins, losses, timeInGame = 0, 0, 0, 0, 0, 0, 0
        msg = 'Daily Report for ' + player + ':\n'
        matches = data.get_matches(player)
        for match in matches:
            created = match['info']['gameCreation']
            diff = time.time() - created / 1000
            if diff < 86400:
                playerData = data.get_player_data(match, player)

                #increment everything
                totalGames += 1
                win = playerData['win']
                if win:
                    wins += 1
                else:
                    losses += 1
                kills += playerData['kills']
                assists += playerData['assists']
                deaths += playerData['deaths']
                timeInGame += match['info']['gameDuration']

                msg += playerData['championName'] + ' - ' + str(playerData['kills']) + '/' + str(playerData['deaths']) + '/' + str(playerData['assists']) + ' - ' + ('Victory' if win else 'Defeat') + '\n'
        
        if totalGames > 0:
            msg += '\nTotal Games: ' + str(totalGames) + ' - KDA: ' + str(kills) + '/' + str(deaths) + '/' + str(assists)
            msg += ' - Winrate: ' + str((wins / (wins + losses)) * 100)[:2] + '% - Time Played: ' + str(int(timeInGame / 60)) + ' Minutes'
            msg += '\n\n'

    if len(report) > 0:
        print('Sending report to Discord...')
        obj = json.loads(json.dumps({'content': report}))
        requests.post(HOOK_URL, data=obj)
    else:
        print('nothing to update')