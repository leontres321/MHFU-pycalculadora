#
from math import *
class Monstruo:
    def __init__(self, nombre, cant_zonas, zonas, defensa, ira):
        self.nombre = nombre
        self.cant_zonas = cant_zonas
        self.zonas = zonas
        self.elemento = {"Fuego":0, "Agua":1, "Trueno":2, "Dragon":3, "Hielo":4}

        #Ver notas del README
        self.defensa = defensa
        self.ira = ira

    #Esto imprime una matriz con los daños de cada zona
    def dano_zonas(self, dano_base_arma, tipo_arma, elem, dano_elem_arma):
        #inicio "matriz"
        #0 = cortante
        if tipo_arma == 0:
            print("|Lugar ||Cortante ||", elem, " || Total |")

        else:
            print("|Lugar ||Contundente ||", elem, " || Total |")

        """
        for i in range(self.cantidad_matriz):
            Var_base = floor(dano_base_arma * self.zonas[i][1] * self.defensa * self.ira) #TODO ver esto bien

        print("Daño cortante en la cara: ", Var_base)
        """

    #solo idea
    def dano_zonas_lanza():
        pass

    def dano_zonas_arco():
        pass
