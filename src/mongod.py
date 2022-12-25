import pymongo

def add_match(matchData):
    connection = get_connection()
    coll = connection.get_database('leagueoflegends').get_collection('matches')
    count = coll.count_documents({'metadata.matchId': matchData['metadata']['matchId']})
    if count == 0:
        coll.insert_one(matchData)
        return True
    connection.close()
    

def get_connection():
    try:
        connection = pymongo.MongoClient("slabby.me")
        return connection
    except:
        print('Could not connect to MongoDB')
        return