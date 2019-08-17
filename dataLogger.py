import threading
import random
import requests

userID = '1'
aquariumName = 'Downstairs'

def temperatureRead():
    return (random.randint(20,26))

def phRead():
    return (random.randint(6,8))

def getValues(): 
    threading.Timer(10, getValues).start()
    temp = temperatureRead()
    ph = phRead()

    try:
        r = requests.post('http://127.0.0.1:5000/data', data = {
            'UserID': userID,
            'Aquarium': aquariumName,
            'Temperature': temp,
            'PH': ph
        })
        r.raise_for_status()
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print (err)

    #print(threading.activeCount())
    #print(threading.enumerate())

