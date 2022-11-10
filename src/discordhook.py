import data, riotapi
import json, requests

HOOK_URL = open('.key', 'r').readlines()[1].strip()

def get_embed(title, description, color=0x04b6c3, image=None, footer=None):
    embed = {
        'title': title, 'description': description, 'color': color, 'image': {'url': image}, 'footer': {'text': footer}
    }
    return embed

def match_embed(match, player):
    playerData = data.get_player_data(match, player)
    win = playerData['win']
    description = playerData['championName'] + '\n'
    description += str(playerData['kills']) + '/' + str(playerData['deaths']) + '/' + str(playerData['assists']) + '\n'
    if playerData['firstBloodKill']:
        description += '*You got First Blood!*\n'
    description += 'Total Damage: ' + str(playerData['totalDamageDealtToChampions']) + '\n'
    description += 'CS: ' + str(playerData['totalMinionsKilled'] + playerData['neutralMinionsKilled']) + '\n'
    description += 'Gold: ' + str(playerData['goldEarned']) + '\n'
    description += 'Vision Score: ' + str(playerData['visionScore']) + '\n'
    description += '**' + ('Victory' if win else 'Defeat') + '**'
    footer = 'Game Duration: ' + str(int(match['info']['gameDuration'] / 60)) + ' Minutes'
    print(playerData['championName'], playerData['championId'])
    embed = get_embed('Match Report for ' + player, description, 0x04b6c3, riotapi.get_champion_image_url(playerData['championName']), footer)
    return embed

def send_hook(content, embed):
    obj = json.loads(json.dumps({'content': content, 'embeds': [embed]}))
    response = requests.post(HOOK_URL, json=obj)
    print(obj, response.text, sep='\n')

# test embeds
if __name__ == '__main__':
    embed = get_embed('Test', 'This is a test', 0x04b6c3, 'https://i.imgur.com/4ZQZ2Zm.png', 'footer test')
    send_hook('Test Embed', embed)