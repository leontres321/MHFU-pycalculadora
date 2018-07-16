from abc import ABCMeta, abstractmethod

class Arma_melee(metaclass = ABCMeta):
    def __init__(self, base, elem, elem_dano, filo_base, filo_elem, clase, var):
        self.base = base
        self.elem_dano = elem_dano
        self.elem = elem
        self.filo_base = filo_base
        self.filo_elem = filo_elem
        self.clase = clase
        self.var = var

    @abstractmethod
    def input_correcto(self):
        pass

    def dano_elem_arma(self):
        return self.elem_dano * self.filo_elem * self.var / 10

    def dano_base_arma(self, input):
        return self.base * self.movimiento[input] * self.filo_base * self.var / self.clase
