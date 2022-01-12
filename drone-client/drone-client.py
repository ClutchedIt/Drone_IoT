import requests
import random
import schedule
from datetime import datetime
import time 

drone = str;

def postdronesend(jsondata):
    r = requests.post('http://localhost:8011/api/drones', json=jsondata) 
    print(r)
    
def error():
    print("Error Encountered")

#creo un metodo fittizio che simula il drone
def dronedemo():
    
    power = random.randrange(0,2)
    velocity = random.randrange(30000,70000) / 1000
    distance = random.randrange(30000,70000) / 1000
    wind = random.randrange(1,500)
    height = random.randrange(1,10000)
    data=datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    idPersona = 1
    idDrone = 1

    if power == 0 :
        velocity=0;
        distance=0;
        height=0;
        drone = 'off';
    else :
        drone = 'on'

    json={
        "dueDate": data,
        "power": power,
        "distance": distance,
        "velocity": velocity,
        "wind": wind,
        "height": height,
        "idPersona":idPersona,
        "idDrone":idDrone,
        "drone": drone
    }
    postdronesend(json)

if __name__ == '__main__':
    #eseguo 
    schedule.every(1).minutes.do(dronedemo)
    while True:
           schedule.run_pending()
           time.sleep(1)