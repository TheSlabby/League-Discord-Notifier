import requests

KEY = open('.key', 'r').readline()
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
    print(response.json())
    return response.json()

def get_match(id):
    url = 'https://americas.api.riotgames.com/lol/match/v5/matches/' + id
    response = requests.get(url, headers=headers)
    return response.json()