import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from datoInflacion import get_dato_inflacion
import math

__version__ = '0.1'

class MyGridLayout(GridLayout):

    # input_monto = ObjectProperty(None)
    # input_n_cuotas = ObjectProperty(None)
    # input_inflacion_anual_estimada = ObjectProperty(None)
    # label_npv = ObjectProperty(None)
    # label_descuento = ObjectProperty(None)
    # label_ahorro = ObjectProperty(None)

    def calcular(self):
        monto_total = float(self.input_monto.text)
        n_cuotas = int(self.input_n_cuotas.text)
        inflacion_estimada = float(self.input_inflacion_anual_estimada.text)

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

        # Clear the input boxes
        # self.monto_total.text = ''
        # self.n_cuotas.text = ''
        # self.inflacion_estimada.text = ''


class Cuotadora(App):
    def build(self):
        return MyGridLayout()

cuotadora = Cuotadora()
cuotadora.run()
