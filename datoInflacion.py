import requests

def get_dato_inflacion():

    r = requests.get('https://cuotadora-default-rtdb.firebaseio.com/.json')
    return r.json()