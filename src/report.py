import data, discordhook, riotapi
import time, requests, json

players = open('players.config', 'r').read().splitlines()
HOOK_URL = open('.key', 'r').readlines()[1].strip()

if __name__ == '__main__':
    print('Getting report for players...')
    for player in players:
        totalGames, kills, deaths, assists, wins, losses, timeInGame = 0, 0, 0, 0, 0, 0, 0
        matches = data.get_matches(player)
        description = ''
        for match in matches:
            created = match['info']['gameCreation']
            diff = time.time() - created / 1000 # convert to seconds
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

                description += (':green_circle: ' if win else ':red_circle: ') + playerData['championName'] + ' - ' + str(playerData['kills']) + '/' + str(playerData['deaths']) + '/' + str(playerData['assists']) + '\n'
        
        if totalGames > 0:
            footer = 'Total Games: ' + str(totalGames) + ' - KDA: ' + str(kills) + '/' + str(deaths) + '/' + str(assists)
            footer += ' - Winrate: ' + str(int((wins / (wins + losses)) * 100)) + '% - Time Played: ' + str(int(timeInGame / 60)) + ' Minutes'
            # send webhook
            embed = discordhook.get_embed('Daily Report for ' + player, description, 0x007d3e, None, footer)
            discordhook.send_hook('', embed)