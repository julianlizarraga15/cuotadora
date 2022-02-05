import requests
from kivy.uix.popup import Popup
import re

def get_dato_inflacion():
    r = requests.get('https://cuotadora-default-rtdb.firebaseio.com/.json')
    return r.json()

def chequear_input_inflacion(inflacion):

    if inflacion.isnumeric():
        return True
    else:
        busqueda = re.search('\d+(\.|\,)\d+', inflacion)
        if busqueda is not None:
            return True
        else:
            popup = ErrorPopup()
            popup.open()
            return False

class ErrorPopup(Popup):
    pass