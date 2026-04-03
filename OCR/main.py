import requests
import random
import time
teamA = 0
teamB = 0

while(True):
    teamA +=1 
    teamB += random(0,10)

    if teamA > 5:
        teamA = 0
    
    if teamB > 10:
        teamB = 0

    time.sleep(1)

    requests.post("http://localhost:3000/update", json={
    "teamA": 4,
    "teamB": 3
    })
