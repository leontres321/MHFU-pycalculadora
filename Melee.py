#Hacer esto para cada arma y contener los combos
from abc import ABCMeta, abstractmethod

class Arma_melee(metaclass = ABCMeta):
    #ver si poner o no var aca, por la falta de var
    def __init__(self, base, elem, elem_dano, filo_base, filo_elem, critico, clase, var):
        self.base = base
        self.elem_dano = elem_dano
        self.elem = elem
        self.filo_base = filo_base
        self.filo_elem = filo_elem
        self.critico = critico
        self.clase = clase
        self.var = var

    @abstractmethod
    #TODO SACAR TIPO CUANDO LOGRE HACER DECENTE LOS ATAQUES
    def dano_base(self, zona, defensa, ira):
        pass

    def dano_elem(self, Ezona, defensa, ira):
        return int(self.elem * self.filo_elem * Ezona * defensa * ira * self.var / 10)
