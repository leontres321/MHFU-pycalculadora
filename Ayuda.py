
class Ayuda:
    def __init__(self):
        self.filo_base = {"rojo": 0.5, "naranjo": 0.75, "amarillo": 1, "verde": 1.125, "azul": 1.25, "blanco": 1.3, "morado": 1.5}
        self.filo_elem = {"rojo": 0.25, "naranjo": 0.5, "amarillo": 0.75, "verde": 1, "azul": 1.0625, "blanco": 1.125, "morado": 1.2}

        #Debe existir una mejor forma de hacer esto... 0 cortante, 1 contundente y 2 ambas, aparte en ingles las recuerdo mas
        self.arma = {"SnS": 0, "LS": 0, "GS": 0, "HH": 1, "DS": 0, "HA": 1, "BOW": 1, "LB": 1, "HB": 1, "LA": 2, "GL": 2}
