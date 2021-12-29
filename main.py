import pandas as pd
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random
import math

# class MyRoot(BoxLayout):
    
#     def __init__(self):
#         super(MyRoot, self).__init__()
    
#     def generate_number(self):
#         self.random_label.text = str(random.randint(0, 1000))

class MyGridLayout(GridLayout):

    def __init__(self, **kwargs):

        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        
        # Set columns
        self.cols = 1

        # Add widgets
        self.add_widget(Label(text='CUOTADORA'))

        # Create a second GridLayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # Add widgets to the second grid
        self.top_grid.add_widget(Label(text='Monto:'))
        self.monto_total = TextInput(multiline=False)
        self.top_grid.add_widget(self.monto_total)

        self.top_grid.add_widget(Label(text='Número de cuotas:'))
        self.n_cuotas = TextInput(multiline=False)
        self.top_grid.add_widget(self.n_cuotas)

        self.top_grid.add_widget(Label(text='Inflación anual estimada:'))
        self.inflacion_estimada = TextInput(multiline=False)
        self.top_grid.add_widget(self.inflacion_estimada)

        # Add the second grid to the main one
        self.add_widget(self.top_grid)

        # Add button to the first grid
        self.calcular = Button(text='Calcular')
        # Bind the button
        self.calcular.bind(on_press=self.press)
        self.add_widget(self.calcular)

        # Create a third GridLayout
        self.bottom_grid = GridLayout()
        self.bottom_grid.cols = 2

        # Add widgets to the third grid
        self.bottom_grid.add_widget(Label(text='Valor presente neto:'))
        self.npv = Label(text='')
        self.bottom_grid.add_widget(self.npv)

        self.bottom_grid.add_widget(Label(text='El descuento es del:'))
        self.descuento = Label(text='')
        self.bottom_grid.add_widget(self.descuento)

        self.bottom_grid.add_widget(Label(text='Te ahorrás:'))
        self.ahorro = Label(text='')
        self.bottom_grid.add_widget(self.ahorro)

        # Add the third grid to the main one
        self.add_widget(self.bottom_grid)

    def press(self, instance):
        monto_total = float(self.monto_total.text)
        n_cuotas = int(self.n_cuotas.text)
        inflacion_estimada = float(self.inflacion_estimada.text)

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
        self.npv.text = '$' + str(vpn)
        self.descuento.text = str(round(porcentaje_descuento, 2)) + '%'
        self.ahorro.text = '$' + str(math.floor(monto_ahorro))

        # Clear the input boxes
        self.monto_total.text = ''
        self.n_cuotas.text = ''
        self.inflacion_estimada.text = ''



class Cuotadora(App):
    def build(self):
        return MyGridLayout()

cuotadora = Cuotadora()
cuotadora.run()
