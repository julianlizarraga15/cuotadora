import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from datoInflacion import get_dato_inflacion, chequear_input_inflacion
from datoInflacion import ErrorPopup
import math

__version__ = '0.1'

class MyGridLayout(GridLayout):

    def calcular(self):

        try:
            monto_total = float(self.input_monto.text)
            n_cuotas = int(self.input_n_cuotas.text)
            inflacion_estimada = self.input_inflacion_anual_estimada.text

            inflacion_ok = chequear_input_inflacion(inflacion_estimada)

            if isinstance(monto_total, float) and isinstance(n_cuotas, int) and inflacion_ok:
                # Convertir a float la inflacion_estimada
                inflacion_estimada = float(inflacion_estimada.replace(',', '.'))
                # Calcular valor presente neto
                inflacion_estimada = inflacion_estimada / 100
                inflacion_mensual = (1 + inflacion_estimada)**(1/12) - 1
                monto_mensual = monto_total / n_cuotas
                vpn = 0
                for cuota in range(n_cuotas):
                    vpn += monto_mensual / ((1+inflacion_mensual)**cuota)
                vpn = math.floor(vpn)

                # Calcular porcentaje de descuento
                porcentaje_descuento = 100 - vpn*100/monto_total

                # Calcular monto ahorrado
                monto_ahorro = monto_total - vpn

                # Print to the screen
                self.ids.label_npv.text = '$' + str(vpn)
                self.ids.label_descuento.text = str(round(porcentaje_descuento, 2)) + '%'
                self.ids.label_ahorro.text = '$' + str(math.floor(monto_ahorro))

        except Exception as e:
            popup = ErrorPopup()
            popup.open()
    

class Cuotadora(App):
    def build(self):
        return MyGridLayout()

cuotadora = Cuotadora()
cuotadora.run()
