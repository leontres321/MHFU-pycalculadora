#
from math import *
class Monstruo:
    def __init__(self, nombre, cantidad_matriz, matriz):
        self.nombre = nombre
        self.cantidad_matriz = cantidad_matriz
        self.matriz = matriz


    #Esto imprime una matriz con los daños de cada zona
    def dano_zonas(self, dano_base_arma, tipo_arma, elem, dano_elem_arma):
        #inicio "matriz"
        #0 = cortante
        if tipo_arma == 0:
            print("|Lugar ||Cortante ||", elem, " || Total |")

        else:
            print("|Lugar ||Contundente ||", elem, " || Total |")

        for i in range(self.cantidad_matriz):
            Var_base = round(dano_base_arma * self.matriz[i][0])

        print("Daño cortante en la cara: ", Var_base)

    #solo idea
    def dano_zonas_lanza():
        pass
