#
from math import *
class Monstruo:
    def __init__(self, nombre, cant_zonas, zonas, defensa, ira):
        self.nombre = nombre
        self.cant_zonas = cant_zonas
        self.zonas = zonas
        self.elemento = {"Fuego":3, "Agua":4, "Trueno":5, "Dragon":6, "Hielo":7}

        #Ver notas del README
        self.defensa = defensa
        self.ira = ira

    #Esto imprime una matriz con los daños de cada zona
    def dano_zonas(self, dano_base_arma, tipo_arma, elem, dano_elem_arma):
        #inicio "matriz"
        #0 = cortante
        #print("Monstruo: {0} / Arma: {1}".format(self.nombre, nombre_arma))

        print("\nMonstruo: {0}".format(self.nombre))
        print("############################")

        if tipo_arma == 0:
            print("|Lugar         ||Cortante    ||", elem, " || Total |")
            zona_dano = 1
        else:
            print("|Lugar         ||Contundente ||", elem, " || Total |")
            zona_dano = 2

        elemento_a_imprimir = self.elemento[elem]


        #loop para imprimir resultados
        for i in range(self.cant_zonas):
            fisico = floor(self.ira * self.defensa * dano_base_arma * self.zonas[i][zona_dano])
            elemental = floor(self.ira * self.defensa * dano_elem_arma * self.zonas[i][elemento_a_imprimir])
            #largo = 14 - len(self.zonas[i[0]]) Largo de la wea para poner espacios vacios
            #TODO ver bien la impresion
            print("|{0} || {1} || {2} || {3} |".format(self.zonas[i][0], fisico, elemental, fisico + elemental))

        print("############################\n")


    #solo idea
    def dano_zonas_lanza():
        pass

    def dano_zonas_arco():
        pass
