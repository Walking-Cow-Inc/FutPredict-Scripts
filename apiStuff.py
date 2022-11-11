import requests
import json

response = requests.get("https://api.football-data.org/v4/competitions/WC/matches?matchday=1",
                        headers={'X-Auth-Token':'fd353439bea048b28af75f97245570f8'})
jsonObj1 = response.json()
jsonObj = jsonObj1['matches']
matchList = []

for each in jsonObj:
    date = each['utcDate'][:10]
    match = each['homeTeam']['shortName'] + ' vs ' + each['awayTeam']['shortName']
    #goals = each['homeTeam']['tla'] + ': ' + (each['score']['fullTime']['home'] if each['score']['fullTime']['home'] != None else '-') + ', ' + each['awayTeam']['tla'] + ': ' + each['score']['fullTime']['away'] if each['score']['fullTime']['away'] != None else '-'
    homeTLA = each['homeTeam']['tla']
    awayTLA = each['awayTeam']['tla']
    homeScore = '-' if each ['score']['fullTime']['home'] == None else ['score']['fullTime']['home']
    awayScore = '-' if each ['score']['fullTime']['away'] == None else ['score']['fullTime']['away']
    goals= homeTLA + ":" + homeScore + " " + awayTLA + ":" + awayScore
    tup = (date, match, goals)
    matchList.append(tup)


for each in matchList:
    print(each)
