import threading
import random


def temperatureRead():
    print (random.randint(20,26))

def phRead():
    print (random.randint(6,8))

def getValues(): 
    threading.Timer(10, getValues).start()
    temperatureRead()
    phRead()





