from abc import ABCMeta, abstractmethod
from parámetros import *
class Melee(metaclass = ABCMeta):
    def __init__(self, ATP, SHARP, ELEMENT, TYPE_ELEMENT, TYPE, CLASS, VAR):  ####### TYPE * VAR pordria guardarse como uno solo
        self.ATP = ATP
        self.SHARP = SHARP
        self.ELEMENT = ELEMENT
        self.TYPE_ELEMENT = TYPE_ELEMENT
        self.TYPE = TYPE
        self.CLASS = CLASS
        self.VAR = VAR

    def dano_base(self):
        pass

    def dano_elemental(self):
        pass

    def dano_total(self,monster):
        lista_danos = []
        for zona in monster.zonas:
            for mov in self.Type: #self.type es diccionario
                dano = (self.ATP * self.TYPE * base_sharp[self.SHARP] * )###########
                print(dano)
                lista_danos.append( None)################3
                #return lista_danos


class Espada_y_Escudo(Melee):
    def __init__(self, parametros):
        super().__init__(parametros,

        class = 1.4, var = 1, ...)
