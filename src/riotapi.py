# interacts with the riot league api
import requests

KEY = open('.key', 'r').readlines()[0].strip()
headers = {
    'X-Riot-Token': KEY
}

def get_id(name):
    url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + name
    response = requests.get(url, headers=headers)
    return response.json()['puuid']

def get_matches(id, count):
    url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/' + id + '/ids?start=0&count=' + str(count)
    response = requests.get(url, headers=headers)
    return response.json()

def get_match(id):
    url = 'https://americas.api.riotgames.com/lol/match/v5/matches/' + id
    response = requests.get(url, headers=headers)
    if response.status_code == 429:
        print('Rate limit exceeded :(')
    return response.json()

def get_champion_image_url(id):
    url = 'http://ddragon.leagueoflegends.com/cdn/11.6.1/img/champion/' + id + '.png'
    return url